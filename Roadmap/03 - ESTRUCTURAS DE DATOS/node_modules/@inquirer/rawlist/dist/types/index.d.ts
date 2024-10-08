import { Separator, type Theme } from '@inquirer/core';
import type { PartialDeep } from '@inquirer/type';
type Choice<Value> = {
    value: Value;
    name?: string;
    key?: string;
};
declare const _default: <Value>(config: {
    message: string;
    choices: readonly (Separator | Choice<Value>)[];
    theme?: PartialDeep<Theme>;
}, context?: import("@inquirer/type").Context) => import("@inquirer/type").CancelablePromise<Value>;
export default _default;
export { Separator } from '@inquirer/core';
