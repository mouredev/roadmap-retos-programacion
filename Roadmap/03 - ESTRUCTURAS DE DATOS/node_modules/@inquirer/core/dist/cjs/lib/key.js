"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.isEnterKey = exports.isNumberKey = exports.isBackspaceKey = exports.isSpaceKey = exports.isDownKey = exports.isUpKey = void 0;
const isUpKey = (key) => 
// The up key
key.name === 'up' ||
    // Vim keybinding
    key.name === 'k' ||
    // Emacs keybinding
    (key.ctrl && key.name === 'p');
exports.isUpKey = isUpKey;
const isDownKey = (key) => 
// The down key
key.name === 'down' ||
    // Vim keybinding
    key.name === 'j' ||
    // Emacs keybinding
    (key.ctrl && key.name === 'n');
exports.isDownKey = isDownKey;
const isSpaceKey = (key) => key.name === 'space';
exports.isSpaceKey = isSpaceKey;
const isBackspaceKey = (key) => key.name === 'backspace';
exports.isBackspaceKey = isBackspaceKey;
const isNumberKey = (key) => '123456789'.includes(key.name);
exports.isNumberKey = isNumberKey;
const isEnterKey = (key) => key.name === 'enter' || key.name === 'return';
exports.isEnterKey = isEnterKey;
