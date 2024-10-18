"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const node_async_hooks_1 = require("node:async_hooks");
const external_editor_1 = require("external-editor");
const core_1 = require("@inquirer/core");
exports.default = (0, core_1.createPrompt)((config, done) => {
    const { waitForUseInput = true, postfix = '.txt', validate = () => true } = config;
    const theme = (0, core_1.makeTheme)(config.theme);
    const [status, setStatus] = (0, core_1.useState)('idle');
    const [value, setValue] = (0, core_1.useState)(config.default || '');
    const [errorMsg, setError] = (0, core_1.useState)();
    const prefix = (0, core_1.usePrefix)({ status, theme });
    function startEditor(rl) {
        rl.pause();
        // Note: The bind call isn't strictly required. But we need it for our mocks to work as expected.
        const editCallback = node_async_hooks_1.AsyncResource.bind((error, answer) => __awaiter(this, void 0, void 0, function* () {
            rl.resume();
            if (error) {
                setError(error.toString());
            }
            else {
                setStatus('loading');
                const isValid = yield validate(answer);
                if (isValid === true) {
                    setError(undefined);
                    setStatus('done');
                    done(answer);
                }
                else {
                    setValue(answer);
                    setError(isValid || 'You must provide a valid value');
                    setStatus('idle');
                }
            }
        }));
        (0, external_editor_1.editAsync)(value, (error, answer) => void editCallback(error, answer), { postfix });
    }
    (0, core_1.useEffect)((rl) => {
        if (!waitForUseInput) {
            startEditor(rl);
        }
    }, []);
    (0, core_1.useKeypress)((key, rl) => {
        // Ignore keypress while our prompt is doing other processing.
        if (status !== 'idle') {
            return;
        }
        if ((0, core_1.isEnterKey)(key)) {
            startEditor(rl);
        }
    });
    const message = theme.style.message(config.message, status);
    let helpTip = '';
    if (status === 'loading') {
        helpTip = theme.style.help('Received');
    }
    else if (status === 'idle') {
        const enterKey = theme.style.key('enter');
        helpTip = theme.style.help(`Press ${enterKey} to launch your preferred editor.`);
    }
    let error = '';
    if (errorMsg) {
        error = theme.style.error(errorMsg);
    }
    return [[prefix, message, helpTip].filter(Boolean).join(' '), error];
});
