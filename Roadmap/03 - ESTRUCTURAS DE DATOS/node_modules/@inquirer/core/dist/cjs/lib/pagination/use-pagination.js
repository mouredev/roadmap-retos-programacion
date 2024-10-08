"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.usePagination = usePagination;
const use_ref_mjs_1 = require('../use-ref.js');
const utils_mjs_1 = require('../utils.js');
const lines_mjs_1 = require('./lines.js');
const position_mjs_1 = require('./position.js');
function usePagination({ items, active, renderItem, pageSize, loop = true, }) {
    const state = (0, use_ref_mjs_1.useRef)({ position: 0, lastActive: 0 });
    const position = loop
        ? (0, position_mjs_1.infinite)({
            active,
            lastActive: state.current.lastActive,
            total: items.length,
            pageSize,
            pointer: state.current.position,
        })
        : (0, position_mjs_1.finite)({
            active,
            total: items.length,
            pageSize,
        });
    state.current.position = position;
    state.current.lastActive = active;
    return (0, lines_mjs_1.lines)({
        items,
        width: (0, utils_mjs_1.readlineWidth)(),
        renderItem,
        active,
        position,
        pageSize,
    }).join('\n');
}
