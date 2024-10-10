"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports._ = void 0;
/* eslint-disable @typescript-eslint/no-explicit-any, @typescript-eslint/no-unsafe-return, @typescript-eslint/no-unsafe-assignment */
const node_readline_1 = __importDefault(require("node:readline"));
const rxjs_1 = require("rxjs");
const run_async_1 = __importDefault(require("run-async"));
const mute_stream_1 = __importDefault(require("mute-stream"));
const core_1 = require("@inquirer/core");
const ansi_escapes_1 = __importDefault(require("ansi-escapes"));
exports._ = {
    set: (obj, path = '', value) => {
        let pointer = obj;
        path.split('.').forEach((key, index, arr) => {
            if (key === '__proto__' || key === 'constructor')
                return;
            if (index === arr.length - 1) {
                pointer[key] = value;
            }
            else if (!(key in pointer) || typeof pointer[key] !== 'object') {
                pointer[key] = {};
            }
            pointer = pointer[key];
        });
    },
    get: (obj, path = '', defaultValue) => {
        const travel = (regexp) => String.prototype.split
            .call(path, regexp)
            .filter(Boolean)
            .reduce(
        // @ts-expect-error implicit any on res[key]
        (res, key) => (res !== null && res !== undefined ? res[key] : res), obj);
        const result = travel(/[,[\]]+?/) || travel(/[,.[\]]+?/);
        return result === undefined || result === obj ? defaultValue : result;
    },
};
/**
 * Resolve a question property value if it is passed as a function.
 * This method will overwrite the property on the question object with the received value.
 */
async function fetchAsyncQuestionProperty(question, prop, answers) {
    const propGetter = question[prop];
    if (typeof propGetter === 'function') {
        return (0, run_async_1.default)(propGetter)(answers);
    }
    return propGetter;
}
class TTYError extends Error {
    name = 'TTYError';
    isTtyError = true;
}
function setupReadlineOptions(opt) {
    // Inquirer 8.x:
    // opt.skipTTYChecks = opt.skipTTYChecks === undefined ? opt.input !== undefined : opt.skipTTYChecks;
    opt.skipTTYChecks = opt.skipTTYChecks === undefined ? true : opt.skipTTYChecks;
    // Default `input` to stdin
    const input = opt.input || process.stdin;
    // Check if prompt is being called in TTY environment
    // If it isn't return a failed promise
    // @ts-expect-error: ignore isTTY type error
    if (!opt.skipTTYChecks && !input.isTTY) {
        throw new TTYError('Prompts can not be meaningfully rendered in non-TTY environments');
    }
    // Add mute capabilities to the output
    const ms = new mute_stream_1.default();
    ms.pipe(opt.output || process.stdout);
    const output = ms;
    return {
        terminal: true,
        ...opt,
        input,
        output,
    };
}
function isQuestionArray(questions) {
    return Array.isArray(questions);
}
function isQuestionMap(questions) {
    return Object.values(questions).every((maybeQuestion) => typeof maybeQuestion === 'object' &&
        !Array.isArray(maybeQuestion) &&
        maybeQuestion != null);
}
function isPromptConstructor(prompt) {
    return Boolean(prompt.prototype &&
        'run' in prompt.prototype &&
        // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
        typeof prompt.prototype.run === 'function');
}
/**
 * Base interface class other can inherits from
 */
class PromptsRunner {
    prompts;
    answers = {};
    process = rxjs_1.EMPTY;
    abortController = new AbortController();
    opt;
    constructor(prompts, opt = {}) {
        this.opt = opt;
        this.prompts = prompts;
    }
    async run(questions, answers) {
        this.abortController = new AbortController();
        // Keep global reference to the answers
        this.answers = typeof answers === 'object' ? { ...answers } : {};
        let obs;
        if (isQuestionArray(questions)) {
            obs = (0, rxjs_1.from)(questions);
        }
        else if ((0, rxjs_1.isObservable)(questions)) {
            obs = questions;
        }
        else if (isQuestionMap(questions)) {
            // Case: Called with a set of { name: question }
            obs = (0, rxjs_1.from)(Object.entries(questions).map(([name, question]) => {
                return Object.assign({}, question, { name });
            }));
        }
        else {
            // Case: Called with a single question config
            obs = (0, rxjs_1.from)([questions]);
        }
        this.process = obs.pipe((0, rxjs_1.concatMap)((question) => (0, rxjs_1.of)(question).pipe((0, rxjs_1.concatMap)((question) => (0, rxjs_1.from)(this.shouldRun(question).then((shouldRun) => {
            if (shouldRun) {
                return question;
            }
            return;
        })).pipe((0, rxjs_1.filter)((val) => val != null))), (0, rxjs_1.concatMap)((question) => (0, rxjs_1.defer)(() => (0, rxjs_1.from)(this.fetchAnswer(question)))))));
        return (0, rxjs_1.lastValueFrom)(this.process.pipe((0, rxjs_1.reduce)((answersObj, answer) => {
            exports._.set(answersObj, answer.name, answer.answer);
            return answersObj;
        }, this.answers)))
            .then(() => this.answers)
            .finally(() => this.close());
    }
    prepareQuestion = async (question) => {
        const [message, defaultValue, resolvedChoices] = await Promise.all([
            fetchAsyncQuestionProperty(question, 'message', this.answers),
            fetchAsyncQuestionProperty(question, 'default', this.answers),
            fetchAsyncQuestionProperty(question, 'choices', this.answers),
        ]);
        let choices;
        if (Array.isArray(resolvedChoices)) {
            choices = resolvedChoices.map((choice) => {
                if (typeof choice === 'string' || typeof choice === 'number') {
                    return { name: choice, value: choice };
                }
                else if (typeof choice === 'object' &&
                    choice != null &&
                    !('value' in choice) &&
                    'name' in choice) {
                    return { ...choice, value: choice.name };
                }
                return choice;
            });
        }
        return Object.assign({}, question, {
            message,
            default: defaultValue,
            choices,
            type: question.type in this.prompts ? question.type : 'input',
        });
    };
    fetchAnswer = async (rawQuestion) => {
        const question = await this.prepareQuestion(rawQuestion);
        const prompt = this.prompts[question.type];
        if (prompt == null) {
            throw new Error(`Prompt for type ${question.type} not found`);
        }
        let cleanupSignal;
        const promptFn = isPromptConstructor(prompt)
            ? (q, opt) => new Promise((resolve, reject) => {
                const { signal } = opt;
                if (signal.aborted) {
                    reject(new core_1.AbortPromptError({ cause: signal.reason }));
                    return;
                }
                const rl = node_readline_1.default.createInterface(setupReadlineOptions(opt));
                /**
                 * Handle the ^C exit
                 */
                const onForceClose = () => {
                    this.close();
                    process.kill(process.pid, 'SIGINT');
                    console.log('');
                };
                const onClose = () => {
                    process.removeListener('exit', onForceClose);
                    rl.removeListener('SIGINT', onForceClose);
                    rl.setPrompt('');
                    rl.output.unmute();
                    rl.output.write(ansi_escapes_1.default.cursorShow);
                    rl.output.end();
                    rl.close();
                };
                // Make sure new prompt start on a newline when closing
                process.on('exit', onForceClose);
                rl.on('SIGINT', onForceClose);
                const activePrompt = new prompt(q, rl, this.answers);
                const cleanup = () => {
                    onClose();
                    cleanupSignal?.();
                };
                const abort = () => {
                    reject(new core_1.AbortPromptError({ cause: signal.reason }));
                    cleanup();
                };
                signal.addEventListener('abort', abort);
                cleanupSignal = () => {
                    signal.removeEventListener('abort', abort);
                    cleanupSignal = undefined;
                };
                activePrompt.run().then(resolve, reject).finally(cleanup);
            })
            : prompt;
        let cleanupModuleSignal;
        const { signal: moduleSignal } = this.opt;
        if (moduleSignal?.aborted) {
            this.abortController.abort(moduleSignal.reason);
        }
        else if (moduleSignal) {
            const abort = () => this.abortController?.abort(moduleSignal.reason);
            moduleSignal.addEventListener('abort', abort);
            cleanupModuleSignal = () => {
                moduleSignal.removeEventListener('abort', abort);
            };
        }
        const { filter = (value) => value } = question;
        const { signal } = this.abortController;
        return promptFn(question, { ...this.opt, signal })
            .then((answer) => ({
            name: question.name,
            answer: filter(answer, this.answers),
        }))
            .finally(() => {
            cleanupSignal?.();
            cleanupModuleSignal?.();
        });
    };
    /**
     * Close the interface and cleanup listeners
     */
    close = () => {
        this.abortController?.abort();
    };
    shouldRun = async (question) => {
        if (question.askAnswered !== true &&
            exports._.get(this.answers, question.name) !== undefined) {
            return false;
        }
        const { when } = question;
        if (typeof when === 'function') {
            const shouldRun = await (0, run_async_1.default)(when)(this.answers);
            return Boolean(shouldRun);
        }
        return when !== false;
    };
}
exports.default = PromptsRunner;
