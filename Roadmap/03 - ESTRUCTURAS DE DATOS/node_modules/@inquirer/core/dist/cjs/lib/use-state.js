"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.useState = useState;
const hook_engine_mjs_1 = require('./hook-engine.js');
function useState(defaultValue) {
    return (0, hook_engine_mjs_1.withPointer)((pointer) => {
        const setFn = (newValue) => {
            // Noop if the value is still the same.
            if (pointer.get() !== newValue) {
                pointer.set(newValue);
                // Trigger re-render
                (0, hook_engine_mjs_1.handleChange)();
            }
        };
        if (pointer.initialized) {
            return [pointer.get(), setFn];
        }
        const value = typeof defaultValue === 'function' ? defaultValue() : defaultValue;
        pointer.set(value);
        return [value, setFn];
    });
}
