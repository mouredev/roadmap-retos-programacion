import { createPrompt, useMemo, useState, useKeypress, usePrefix, isEnterKey, Separator, makeTheme, } from '@inquirer/core';
import colors from 'yoctocolors-cjs';
const numberRegex = /\d+/;
function isSelectableChoice(choice) {
    return choice != null && !Separator.isSeparator(choice);
}
function normalizeChoices(choices) {
    let index = 0;
    return choices.map((choice) => {
        if (Separator.isSeparator(choice))
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
        const name = choice.name ?? String(choice.value);
        return {
            value: choice.value,
            name,
            short: choice.short ?? name,
            key: choice.key ?? String(index),
        };
    });
}
export default createPrompt((config, done) => {
    const choices = useMemo(() => normalizeChoices(config.choices), [config.choices]);
    const [status, setStatus] = useState('idle');
    const [value, setValue] = useState('');
    const [errorMsg, setError] = useState();
    const theme = makeTheme(config.theme);
    const prefix = usePrefix({ status, theme });
    useKeypress((key, rl) => {
        if (isEnterKey(key)) {
            let selectedChoice;
            if (numberRegex.test(value)) {
                const answer = Number.parseInt(value, 10) - 1;
                selectedChoice = choices.filter(isSelectableChoice)[answer];
            }
            else {
                selectedChoice = choices.find((choice) => isSelectableChoice(choice) && choice.key === value);
            }
            if (isSelectableChoice(selectedChoice)) {
                setValue(selectedChoice.short ?? selectedChoice.name ?? String(selectedChoice.value));
                setStatus('done');
                done(selectedChoice.value);
            }
            else if (value === '') {
                setError('Please input a value');
            }
            else {
                setError(`"${colors.red(value)}" isn't an available option`);
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
        if (Separator.isSeparator(choice)) {
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
export { Separator } from '@inquirer/core';
