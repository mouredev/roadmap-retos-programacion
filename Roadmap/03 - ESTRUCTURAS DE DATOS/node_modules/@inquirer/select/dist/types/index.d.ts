import { Separator, type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type SelectTheme = {
    icon: {
        cursor: string;
    };
    style: {
        disabled: (text: string) => string;
    };
    helpMode: 'always' | 'never' | 'auto';
};
type Choice<Value> = {
    value: Value;
    name?: string;
    description?: string;
    disabled?: boolean | string;
    type?: never;
};
declare const _default: <Value>(config: {
    message: string;
    choices: readonly (Separator | Choice<Value>)[];
    pageSize?: number;
    loop?: boolean;
    default?: unknown;
    theme?: PartialDeep<Theme<SelectTheme>>;
}, context?: import("@inquirer/type").Context) => import("@inquirer/type").CancelablePromise<Value>;
export default _default;
export { Separator } from '@inquirer/core';
