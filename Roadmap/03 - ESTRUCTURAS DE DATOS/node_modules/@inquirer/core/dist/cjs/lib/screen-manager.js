"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const strip_ansi_1 = __importDefault(require("strip-ansi"));
const ansi_escapes_1 = __importDefault(require("ansi-escapes"));
const utils_mjs_1 = require('./utils.js');
const height = (content) => content.split('\n').length;
const lastLine = (content) => { var _a; return (_a = content.split('\n').pop()) !== null && _a !== void 0 ? _a : ''; };
function cursorDown(n) {
    return n > 0 ? ansi_escapes_1.default.cursorDown(n) : '';
}
class ScreenManager {
    constructor(rl) {
        Object.defineProperty(this, "rl", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: rl
        });
        // These variables are keeping information to allow correct prompt re-rendering
        Object.defineProperty(this, "height", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 0
        });
        Object.defineProperty(this, "extraLinesUnderPrompt", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 0
        });
        Object.defineProperty(this, "cursorPos", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        this.rl = rl;
        this.cursorPos = rl.getCursorPos();
    }
    write(content) {
        this.rl.output.unmute();
        this.rl.output.write(content);
        this.rl.output.mute();
    }
    render(content, bottomContent = '') {
        // Write message to screen and setPrompt to control backspace
        const promptLine = lastLine(content);
        const rawPromptLine = (0, strip_ansi_1.default)(promptLine);
        // Remove the rl.line from our prompt. We can't rely on the content of
        // rl.line (mainly because of the password prompt), so just rely on it's
        // length.
        let prompt = rawPromptLine;
        if (this.rl.line.length > 0) {
            prompt = prompt.slice(0, -this.rl.line.length);
        }
        this.rl.setPrompt(prompt);
        // SetPrompt will change cursor position, now we can get correct value
        this.cursorPos = this.rl.getCursorPos();
        const width = (0, utils_mjs_1.readlineWidth)();
        content = (0, utils_mjs_1.breakLines)(content, width);
        bottomContent = (0, utils_mjs_1.breakLines)(bottomContent, width);
        // Manually insert an extra line if we're at the end of the line.
        // This prevent the cursor from appearing at the beginning of the
        // current line.
        if (rawPromptLine.length % width === 0) {
            content += '\n';
        }
        let output = content + (bottomContent ? '\n' + bottomContent : '');
        /**
         * Re-adjust the cursor at the correct position.
         */
        // We need to consider parts of the prompt under the cursor as part of the bottom
        // content in order to correctly cleanup and re-render.
        const promptLineUpDiff = Math.floor(rawPromptLine.length / width) - this.cursorPos.rows;
        const bottomContentHeight = promptLineUpDiff + (bottomContent ? height(bottomContent) : 0);
        // Return cursor to the input position (on top of the bottomContent)
        if (bottomContentHeight > 0)
            output += ansi_escapes_1.default.cursorUp(bottomContentHeight);
        // Return cursor to the initial left offset.
        output += ansi_escapes_1.default.cursorTo(this.cursorPos.cols);
        /**
         * Render and store state for future re-rendering
         */
        this.write(cursorDown(this.extraLinesUnderPrompt) +
            ansi_escapes_1.default.eraseLines(this.height) +
            output);
        this.extraLinesUnderPrompt = bottomContentHeight;
        this.height = height(output);
    }
    checkCursorPos() {
        const cursorPos = this.rl.getCursorPos();
        if (cursorPos.cols !== this.cursorPos.cols) {
            this.write(ansi_escapes_1.default.cursorTo(cursorPos.cols));
            this.cursorPos = cursorPos;
        }
    }
    done({ clearContent }) {
        this.rl.setPrompt('');
        let output = cursorDown(this.extraLinesUnderPrompt);
        output += clearContent ? ansi_escapes_1.default.eraseLines(this.height) : '\n';
        output += ansi_escapes_1.default.cursorShow;
        this.write(output);
        this.rl.close();
    }
}
exports.default = ScreenManager;
