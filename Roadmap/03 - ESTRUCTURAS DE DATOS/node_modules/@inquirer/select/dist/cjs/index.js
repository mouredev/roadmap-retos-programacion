"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Separator = void 0;
const core_1 = require("@inquirer/core");
const yoctocolors_cjs_1 = __importDefault(require("yoctocolors-cjs"));
const figures_1 = __importDefault(require("@inquirer/figures"));
const ansi_escapes_1 = __importDefault(require("ansi-escapes"));
const selectTheme = {
    icon: { cursor: figures_1.default.pointer },
    style: {
        disabled: (text) => yoctocolors_cjs_1.default.dim(`- ${text}`),
        description: (text) => yoctocolors_cjs_1.default.cyan(text),
    },
    helpMode: 'auto',
};
function isSelectable(item) {
    return !core_1.Separator.isSeparator(item) && !item.disabled;
}
function normalizeChoices(choices) {
    return choices.map((choice) => {
        var _a, _b, _c;
        if (core_1.Separator.isSeparator(choice))
            return choice;
        if (typeof choice === 'string') {
            return {
                value: choice,
                name: choice,
                short: choice,
                disabled: false,
            };
        }
        const name = (_a = choice.name) !== null && _a !== void 0 ? _a : String(choice.value);
        return {
            value: choice.value,
            name,
            description: choice.description,
            short: (_b = choice.short) !== null && _b !== void 0 ? _b : name,
            disabled: (_c = choice.disabled) !== null && _c !== void 0 ? _c : false,
        };
    });
}
exports.default = (0, core_1.createPrompt)((config, done) => {
    const { loop = true, pageSize = 7 } = config;
    const firstRender = (0, core_1.useRef)(true);
    const theme = (0, core_1.makeTheme)(selectTheme, config.theme);
    const [status, setStatus] = (0, core_1.useState)('idle');
    const prefix = (0, core_1.usePrefix)({ status, theme });
    const searchTimeoutRef = (0, core_1.useRef)();
    const items = (0, core_1.useMemo)(() => normalizeChoices(config.choices), [config.choices]);
    const bounds = (0, core_1.useMemo)(() => {
        const first = items.findIndex(isSelectable);
        const last = items.findLastIndex(isSelectable);
        if (first < 0) {
            throw new core_1.ValidationError('[select prompt] No selectable choices. All choices are disabled.');
        }
        return { first, last };
    }, [items]);
    const defaultItemIndex = (0, core_1.useMemo)(() => {
        if (!('default' in config))
            return -1;
        return items.findIndex((item) => isSelectable(item) && item.value === config.default);
    }, [config.default, items]);
    const [active, setActive] = (0, core_1.useState)(defaultItemIndex === -1 ? bounds.first : defaultItemIndex);
    // Safe to assume the cursor position always point to a Choice.
    const selectedChoice = items[active];
    (0, core_1.useKeypress)((key, rl) => {
        clearTimeout(searchTimeoutRef.current);
        if ((0, core_1.isEnterKey)(key)) {
            setStatus('done');
            done(selectedChoice.value);
        }
        else if ((0, core_1.isUpKey)(key) || (0, core_1.isDownKey)(key)) {
            rl.clearLine(0);
            if (loop ||
                ((0, core_1.isUpKey)(key) && active !== bounds.first) ||
                ((0, core_1.isDownKey)(key) && active !== bounds.last)) {
                const offset = (0, core_1.isUpKey)(key) ? -1 : 1;
                let next = active;
                do {
                    next = (next + offset + items.length) % items.length;
                } while (!isSelectable(items[next]));
                setActive(next);
            }
        }
        else if ((0, core_1.isNumberKey)(key)) {
            rl.clearLine(0);
            const position = Number(key.name) - 1;
            const item = items[position];
            if (item != null && isSelectable(item)) {
                setActive(position);
            }
        }
        else if ((0, core_1.isBackspaceKey)(key)) {
            rl.clearLine(0);
        }
        else {
            // Default to search
            const searchTerm = rl.line.toLowerCase();
            const matchIndex = items.findIndex((item) => {
                if (core_1.Separator.isSeparator(item) || !isSelectable(item))
                    return false;
                return item.name.toLowerCase().startsWith(searchTerm);
            });
            if (matchIndex >= 0) {
                setActive(matchIndex);
            }
            searchTimeoutRef.current = setTimeout(() => {
                rl.clearLine(0);
            }, 700);
        }
    });
    (0, core_1.useEffect)(() => () => {
        clearTimeout(searchTimeoutRef.current);
    }, []);
    const message = theme.style.message(config.message, status);
    let helpTipTop = '';
    let helpTipBottom = '';
    if (theme.helpMode === 'always' ||
        (theme.helpMode === 'auto' && firstRender.current)) {
        firstRender.current = false;
        if (items.length > pageSize) {
            helpTipBottom = `\n${theme.style.help('(Use arrow keys to reveal more choices)')}`;
        }
        else {
            helpTipTop = theme.style.help('(Use arrow keys)');
        }
    }
    const page = (0, core_1.usePagination)({
        items,
        active,
        renderItem({ item, isActive }) {
            if (core_1.Separator.isSeparator(item)) {
                return ` ${item.separator}`;
            }
            if (item.disabled) {
                const disabledLabel = typeof item.disabled === 'string' ? item.disabled : '(disabled)';
                return theme.style.disabled(`${item.name} ${disabledLabel}`);
            }
            const color = isActive ? theme.style.highlight : (x) => x;
            const cursor = isActive ? theme.icon.cursor : ` `;
            return color(`${cursor} ${item.name}`);
        },
        pageSize,
        loop,
    });
    if (status === 'done') {
        return `${prefix} ${message} ${theme.style.answer(selectedChoice.short)}`;
    }
    const choiceDescription = selectedChoice.description
        ? `\n${theme.style.description(selectedChoice.description)}`
        : ``;
    return `${[prefix, message, helpTipTop].filter(Boolean).join(' ')}\n${page}${helpTipBottom}${choiceDescription}${ansi_escapes_1.default.cursorHide}`;
});
var core_2 = require("@inquirer/core");
Object.defineProperty(exports, "Separator", { enumerable: true, get: function () { return core_2.Separator; } });
