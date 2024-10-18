"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Separator = void 0;
const core_1 = require("@inquirer/core");
const yoctocolors_cjs_1 = __importDefault(require("yoctocolors-cjs"));
const numberRegex = /\d+/;
function isSelectableChoice(choice) {
    return choice != null && !core_1.Separator.isSeparator(choice);
}
function normalizeChoices(choices) {
    let index = 0;
    return choices.map((choice) => {
        var _a, _b, _c;
        if (core_1.Separator.isSeparator(choice))
            return choice;
        index += 1;
        if (typeof choice === 'string') {
            return {
                value: choice,
                name: choice,
                short: choice,
                key: String(index),
            };
        }
        const name = (_a = choice.name) !== null && _a !== void 0 ? _a : String(choice.value);
        return {
            value: choice.value,
            name,
            short: (_b = choice.short) !== null && _b !== void 0 ? _b : name,
            key: (_c = choice.key) !== null && _c !== void 0 ? _c : String(index),
        };
    });
}
exports.default = (0, core_1.createPrompt)((config, done) => {
    const choices = (0, core_1.useMemo)(() => normalizeChoices(config.choices), [config.choices]);
    const [status, setStatus] = (0, core_1.useState)('idle');
    const [value, setValue] = (0, core_1.useState)('');
    const [errorMsg, setError] = (0, core_1.useState)();
    const theme = (0, core_1.makeTheme)(config.theme);
    const prefix = (0, core_1.usePrefix)({ status, theme });
    (0, core_1.useKeypress)((key, rl) => {
        var _a, _b;
        if ((0, core_1.isEnterKey)(key)) {
            let selectedChoice;
            if (numberRegex.test(value)) {
                const answer = Number.parseInt(value, 10) - 1;
                selectedChoice = choices.filter(isSelectableChoice)[answer];
            }
            else {
                selectedChoice = choices.find((choice) => isSelectableChoice(choice) && choice.key === value);
            }
            if (isSelectableChoice(selectedChoice)) {
                setValue((_b = (_a = selectedChoice.short) !== null && _a !== void 0 ? _a : selectedChoice.name) !== null && _b !== void 0 ? _b : String(selectedChoice.value));
                setStatus('done');
                done(selectedChoice.value);
            }
            else if (value === '') {
                setError('Please input a value');
            }
            else {
                setError(`"${yoctocolors_cjs_1.default.red(value)}" isn't an available option`);
            }
        }
        else {
            setValue(rl.line);
            setError(undefined);
        }
    });
    const message = theme.style.message(config.message, status);
    if (status === 'done') {
        return `${prefix} ${message} ${theme.style.answer(value)}`;
    }
    const choicesStr = choices
        .map((choice) => {
        if (core_1.Separator.isSeparator(choice)) {
            return ` ${choice.separator}`;
        }
        const line = `  ${choice.key}) ${choice.name}`;
        if (choice.key === value.toLowerCase()) {
            return theme.style.highlight(line);
        }
        return line;
    })
        .join('\n');
    let error = '';
    if (errorMsg) {
        error = theme.style.error(errorMsg);
    }
    return [
        `${prefix} ${message} ${value}`,
        [choicesStr, error].filter(Boolean).join('\n'),
    ];
});
var core_2 = require("@inquirer/core");
Object.defineProperty(exports, "Separator", { enumerable: true, get: function () { return core_2.Separator; } });
