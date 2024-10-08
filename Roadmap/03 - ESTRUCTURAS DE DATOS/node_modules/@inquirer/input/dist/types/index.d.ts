import { type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type InputConfig = {
    message: string;
    default?: string;
    required?: boolean;
    transformer?: (value: string, { isFinal }: {
        isFinal: boolean;
    }) => string;
    validate?: (value: string) => boolean | string | Promise<string | boolean>;
    theme?: PartialDeep<Theme>;
};
declare const _default: import("@inquirer/type").Prompt<string, InputConfig>;
export default _default;
