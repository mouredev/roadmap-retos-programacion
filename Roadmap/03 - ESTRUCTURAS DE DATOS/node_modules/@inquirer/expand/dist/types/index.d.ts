import { type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type ExpandChoice = {
    key: string;
    name: string;
} | {
    key: string;
    value: string;
} | {
    key: string;
    name: string;
    value: string;
};
type ExpandConfig = {
    message: string;
    choices: ReadonlyArray<ExpandChoice>;
    default?: string;
    expanded?: boolean;
    theme?: PartialDeep<Theme>;
};
declare const _default: import("@inquirer/type").Prompt<string, ExpandConfig>;
export default _default;
