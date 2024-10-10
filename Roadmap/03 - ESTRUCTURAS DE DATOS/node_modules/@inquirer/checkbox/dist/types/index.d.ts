import { Separator, type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type CheckboxTheme = {
    icon: {
        checked: string;
        unchecked: string;
        cursor: string;
    };
    style: {
        disabledChoice: (text: string) => string;
        renderSelectedChoices: <T>(selectedChoices: ReadonlyArray<Choice<T>>, allChoices: ReadonlyArray<Choice<T> | Separator>) => string;
    };
    helpMode: 'always' | 'never' | 'auto';
};
type Choice<Value> = {
    name?: string;
    value: Value;
    disabled?: boolean | string;
    checked?: boolean;
    type?: never;
};
type Item<Value> = Separator | Choice<Value>;
declare const _default: <Value>(config: {
    message: string;
    prefix?: string;
    pageSize?: number;
    instructions?: string | boolean;
    choices: readonly (Separator | Choice<Value>)[];
    loop?: boolean;
    required?: boolean;
    validate?: ((items: readonly Item<Value>[]) => boolean | string | Promise<string | boolean>) | undefined;
    theme?: PartialDeep<Theme<CheckboxTheme>>;
}, context?: import("@inquirer/type").Context) => import("@inquirer/type").CancelablePromise<Value[]>;
export default _default;
export { Separator } from '@inquirer/core';
