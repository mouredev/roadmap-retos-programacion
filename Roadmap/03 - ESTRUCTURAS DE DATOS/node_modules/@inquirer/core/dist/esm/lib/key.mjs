export const isUpKey = (key) => 
// The up key
key.name === 'up' ||
    // Vim keybinding
    key.name === 'k' ||
    // Emacs keybinding
    (key.ctrl && key.name === 'p');
export const isDownKey = (key) => 
// The down key
key.name === 'down' ||
    // Vim keybinding
    key.name === 'j' ||
    // Emacs keybinding
    (key.ctrl && key.name === 'n');
export const isSpaceKey = (key) => key.name === 'space';
export const isBackspaceKey = (key) => key.name === 'backspace';
export const isNumberKey = (key) => '123456789'.includes(key.name);
export const isEnterKey = (key) => key.name === 'enter' || key.name === 'return';
