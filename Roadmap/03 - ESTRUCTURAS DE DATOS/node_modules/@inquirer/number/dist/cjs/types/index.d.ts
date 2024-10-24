import { type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type NumberConfig = {
    message: string;
    default?: number;
    min?: number;
    max?: number;
    step?: number | 'any';
    required?: boolean;
    validate?: (value: number | undefined) => boolean | string | Promise<string | boolean>;
    theme?: PartialDeep<Theme>;
};
declare const _default: import("@inquirer/type").Prompt<number | undefined, NumberConfig>;
export default _default;
