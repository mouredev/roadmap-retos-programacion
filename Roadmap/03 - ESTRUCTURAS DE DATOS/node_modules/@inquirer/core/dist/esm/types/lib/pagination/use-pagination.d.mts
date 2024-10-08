import type { Prettify } from '@inquirer/type';
import { type Theme } from '../theme.mjs';
import { type Layout } from './lines.mjs';
export declare function usePagination<T>({ items, active, renderItem, pageSize, loop, }: {
    items: ReadonlyArray<T>;
    /** The index of the active item. */
    active: number;
    /** Renders an item as part of a page. */
    renderItem: (layout: Prettify<Layout<T>>) => string;
    /** The size of the page. */
    pageSize: number;
    /** Allows creating an infinitely looping list. `true` if unspecified. */
    loop?: boolean;
    theme?: Theme;
}): string;
