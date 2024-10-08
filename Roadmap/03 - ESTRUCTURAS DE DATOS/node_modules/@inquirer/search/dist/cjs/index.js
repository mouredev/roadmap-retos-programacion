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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Separator = void 0;
const core_1 = require("@inquirer/core");
const yoctocolors_cjs_1 = __importDefault(require("yoctocolors-cjs"));
const figures_1 = __importDefault(require("@inquirer/figures"));
const searchTheme = {
    icon: { cursor: figures_1.default.pointer },
    style: {
        disabled: (text) => yoctocolors_cjs_1.default.dim(`- ${text}`),
        searchTerm: (text) => yoctocolors_cjs_1.default.cyan(text),
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
    var _a;
    const { pageSize = 7, validate = () => true } = config;
    const theme = (0, core_1.makeTheme)(searchTheme, config.theme);
    const firstRender = (0, core_1.useRef)(true);
    const [status, setStatus] = (0, core_1.useState)('loading');
    const [searchTerm, setSearchTerm] = (0, core_1.useState)('');
    const [searchResults, setSearchResults] = (0, core_1.useState)([]);
    const [searchError, setSearchError] = (0, core_1.useState)();
    const prefix = (0, core_1.usePrefix)({ status, theme });
    const bounds = (0, core_1.useMemo)(() => {
        const first = searchResults.findIndex(isSelectable);
        const last = searchResults.findLastIndex(isSelectable);
        return { first, last };
    }, [searchResults]);
    const [active = bounds.first, setActive] = (0, core_1.useState)();
    (0, core_1.useEffect)(() => {
        const controller = new AbortController();
        setStatus('loading');
        setSearchError(undefined);
        const fetchResults = () => __awaiter(void 0, void 0, void 0, function* () {
            try {
                const results = yield config.source(searchTerm || undefined, {
                    signal: controller.signal,
                });
                if (!controller.signal.aborted) {
                    // Reset the pointer
                    setActive(undefined);
                    setSearchError(undefined);
                    setSearchResults(normalizeChoices(results));
                    setStatus('idle');
                }
            }
            catch (error) {
                if (!controller.signal.aborted && error instanceof Error) {
                    setSearchError(error.message);
                }
            }
        });
        void fetchResults();
        return () => {
            controller.abort();
        };
    }, [searchTerm]);
    // Safe to assume the cursor position never points to a Separator.
    const selectedChoice = searchResults[active];
    (0, core_1.useKeypress)((key, rl) => __awaiter(void 0, void 0, void 0, function* () {
        if ((0, core_1.isEnterKey)(key)) {
            if (selectedChoice) {
                setStatus('loading');
                const isValid = yield validate(selectedChoice.value);
                setStatus('idle');
                if (isValid === true) {
                    setStatus('done');
                    done(selectedChoice.value);
                }
                else if (selectedChoice.name === searchTerm) {
                    setSearchError(isValid || 'You must provide a valid value');
                }
                else {
                    // Reset line with new search term
                    rl.write(selectedChoice.name);
                    setSearchTerm(selectedChoice.name);
                }
            }
            else {
                // Reset the readline line value to the previous value. On line event, the value
                // get cleared, forcing the user to re-enter the value instead of fixing it.
                rl.write(searchTerm);
            }
        }
        else if (key.name === 'tab' && selectedChoice) {
            rl.clearLine(0); // Remove the tab character.
            rl.write(selectedChoice.name);
            setSearchTerm(selectedChoice.name);
        }
        else if (status !== 'loading' && (key.name === 'up' || key.name === 'down')) {
            rl.clearLine(0);
            if ((key.name === 'up' && active !== bounds.first) ||
                (key.name === 'down' && active !== bounds.last)) {
                const offset = key.name === 'up' ? -1 : 1;
                let next = active;
                do {
                    next = (next + offset + searchResults.length) % searchResults.length;
                } while (!isSelectable(searchResults[next]));
                setActive(next);
            }
        }
        else {
            setSearchTerm(rl.line);
        }
    }));
    const message = theme.style.message(config.message, status);
    if (active > 0) {
        firstRender.current = false;
    }
    let helpTip = '';
    if (searchResults.length > 1 &&
        (theme.helpMode === 'always' || (theme.helpMode === 'auto' && firstRender.current))) {
        helpTip =
            searchResults.length > pageSize
                ? `\n${theme.style.help('(Use arrow keys to reveal more choices)')}`
                : `\n${theme.style.help('(Use arrow keys)')}`;
    }
    // TODO: What to do if no results are found? Should we display a message?
    const page = (0, core_1.usePagination)({
        items: searchResults,
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
        loop: false,
    });
    let error;
    if (searchError) {
        error = theme.style.error(searchError);
    }
    else if (searchResults.length === 0 && searchTerm !== '' && status === 'idle') {
        error = theme.style.error('No results found');
    }
    let searchStr;
    if (status === 'done' && selectedChoice) {
        const answer = (_a = selectedChoice.short) !== null && _a !== void 0 ? _a : selectedChoice.name;
        return `${prefix} ${message} ${theme.style.answer(answer)}`;
    }
    else {
        searchStr = theme.style.searchTerm(searchTerm);
    }
    const choiceDescription = (selectedChoice === null || selectedChoice === void 0 ? void 0 : selectedChoice.description)
        ? `\n${theme.style.description(selectedChoice.description)}`
        : ``;
    return [
        [prefix, message, searchStr].filter(Boolean).join(' '),
        `${error !== null && error !== void 0 ? error : page}${helpTip}${choiceDescription}`,
    ];
});
var core_2 = require("@inquirer/core");
Object.defineProperty(exports, "Separator", { enumerable: true, get: function () { return core_2.Separator; } });
