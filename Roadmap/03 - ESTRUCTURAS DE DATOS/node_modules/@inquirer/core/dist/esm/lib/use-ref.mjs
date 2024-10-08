import { useState } from './use-state.mjs';
export function useRef(val) {
    return useState({ current: val })[0];
}
