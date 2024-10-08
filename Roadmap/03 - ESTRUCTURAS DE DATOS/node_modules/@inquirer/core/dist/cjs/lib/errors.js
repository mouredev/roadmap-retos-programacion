"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.ValidationError = exports.HookError = exports.ExitPromptError = exports.CancelPromptError = exports.AbortPromptError = void 0;
class AbortPromptError extends Error {
    constructor(options) {
        super();
        Object.defineProperty(this, "name", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'AbortPromptError'
        });
        Object.defineProperty(this, "message", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'Prompt was aborted'
        });
        this.cause = options === null || options === void 0 ? void 0 : options.cause;
    }
}
exports.AbortPromptError = AbortPromptError;
class CancelPromptError extends Error {
    constructor() {
        super(...arguments);
        Object.defineProperty(this, "name", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'CancelPromptError'
        });
        Object.defineProperty(this, "message", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'Prompt was canceled'
        });
    }
}
exports.CancelPromptError = CancelPromptError;
class ExitPromptError extends Error {
    constructor() {
        super(...arguments);
        Object.defineProperty(this, "name", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'ExitPromptError'
        });
    }
}
exports.ExitPromptError = ExitPromptError;
class HookError extends Error {
    constructor() {
        super(...arguments);
        Object.defineProperty(this, "name", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'HookError'
        });
    }
}
exports.HookError = HookError;
class ValidationError extends Error {
    constructor() {
        super(...arguments);
        Object.defineProperty(this, "name", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'ValidationError'
        });
    }
}
exports.ValidationError = ValidationError;
