import { Separator, type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type SelectTheme = {
    icon: {
        cursor: string;
    };
    style: {
        disabled: (text: string) => string;
        description: (text: string) => string;
    };
    helpMode: 'always' | 'never' | 'auto';
};
type Choice<Value> = {
    value: Value;
    name?: string;
    description?: string;
    short?: string;
    disabled?: boolean | string;
    type?: never;
};
declare const _default: <Value>(config: {
    message: string;
    choices: readonly (string | Separator)[] | readonly (Separator | Choice<Value>)[];
    pageSize?: number | undefined;
    loop?: boolean | undefined;
    default?: unknown;
    theme?: PartialDeep<Theme<SelectTheme>> | undefined;
}, context?: import("@inquirer/type").Context) => Promise<Value> & {
    cancel: () => void;
};
export default _default;
export { Separator } from '@inquirer/core';
