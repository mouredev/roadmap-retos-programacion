import { type Prettify } from '@inquirer/type';
/** Represents an item that's part of a layout, about to be rendered */
export type Layout<T> = {
    item: T;
    index: number;
    isActive: boolean;
};
/**
 * Renders a page of items as lines that fit within the given width ensuring
 * that the number of lines is not greater than the page size, and the active
 * item renders at the provided position, while prioritizing that as many lines
 * of the active item get rendered as possible.
 */
export declare function lines<T>({ items, width, renderItem, active, position: requested, pageSize, }: {
    items: ReadonlyArray<T>;
    /** The width of a rendered line in characters. */
    width: number;
    /** Renders an item as part of a page. */
    renderItem: (layout: Prettify<Layout<T>>) => string;
    /** The index of the active item in the list of items. */
    active: number;
    /** The position on the page at which to render the active item. */
    position: number;
    /** The number of lines to render per page. */
    pageSize: number;
}): string[];
