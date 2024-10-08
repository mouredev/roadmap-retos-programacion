import { type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type EditorConfig = {
    message: string;
    default?: string;
    postfix?: string;
    waitForUseInput?: boolean;
    validate?: (value: string) => boolean | string | Promise<string | boolean>;
    theme?: PartialDeep<Theme>;
};
declare const _default: import("@inquirer/type").Prompt<string, EditorConfig>;
export default _default;
