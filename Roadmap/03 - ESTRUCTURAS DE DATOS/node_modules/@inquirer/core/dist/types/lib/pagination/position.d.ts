/**
 * Creates the next position for the active item considering a finite list of
 * items to be rendered on a page.
 */
export declare function finite({ active, pageSize, total, }: {
    active: number;
    pageSize: number;
    total: number;
}): number;
/**
 * Creates the next position for the active item considering an infinitely
 * looping list of items to be rendered on the page.
 */
export declare function infinite({ active, lastActive, total, pageSize, pointer, }: {
    active: number;
    lastActive: number;
    total: number;
    pageSize: number;
    pointer: number;
}): number;
