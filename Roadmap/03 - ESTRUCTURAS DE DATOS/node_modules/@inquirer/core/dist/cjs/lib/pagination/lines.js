"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.lines = lines;
const utils_mjs_1 = require('../utils.js');
function split(content, width) {
    return (0, utils_mjs_1.breakLines)(content, width).split('\n');
}
/**
 * Rotates an array of items by an integer number of positions.
 * @param {number} count The number of positions to rotate by
 * @param {T[]} items The items to rotate
 */
function rotate(count, items) {
    const max = items.length;
    const offset = ((count % max) + max) % max;
    return [...items.slice(offset), ...items.slice(0, offset)];
}
/**
 * Renders a page of items as lines that fit within the given width ensuring
 * that the number of lines is not greater than the page size, and the active
 * item renders at the provided position, while prioritizing that as many lines
 * of the active item get rendered as possible.
 */
function lines({ items, width, renderItem, active, position: requested, pageSize, }) {
    const layouts = items.map((item, index) => ({
        item,
        index,
        isActive: index === active,
    }));
    const layoutsInPage = rotate(active - requested, layouts).slice(0, pageSize);
    const renderItemAt = (index) => layoutsInPage[index] == null ? [] : split(renderItem(layoutsInPage[index]), width);
    // Create a blank array of lines for the page
    const pageBuffer = Array.from({ length: pageSize });
    // Render the active item to decide the position
    const activeItem = renderItemAt(requested).slice(0, pageSize);
    const position = requested + activeItem.length <= pageSize ? requested : pageSize - activeItem.length;
    // Add the lines of the active item into the page
    pageBuffer.splice(position, activeItem.length, ...activeItem);
    // Fill the page under the active item
    let bufferPointer = position + activeItem.length;
    let layoutPointer = requested + 1;
    while (bufferPointer < pageSize && layoutPointer < layoutsInPage.length) {
        for (const line of renderItemAt(layoutPointer)) {
            pageBuffer[bufferPointer++] = line;
            if (bufferPointer >= pageSize)
                break;
        }
        layoutPointer++;
    }
    // Fill the page over the active item
    bufferPointer = position - 1;
    layoutPointer = requested - 1;
    while (bufferPointer >= 0 && layoutPointer >= 0) {
        for (const line of renderItemAt(layoutPointer).reverse()) {
            pageBuffer[bufferPointer--] = line;
            if (bufferPointer < 0)
                break;
        }
        layoutPointer--;
    }
    return pageBuffer.filter((line) => typeof line === 'string');
}
