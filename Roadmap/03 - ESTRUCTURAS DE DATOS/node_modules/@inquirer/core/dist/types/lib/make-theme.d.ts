import type { Prettify, PartialDeep } from '@inquirer/type';
import { type Theme } from './theme.js';
export declare function makeTheme<SpecificTheme extends object>(...themes: ReadonlyArray<undefined | PartialDeep<Theme<SpecificTheme>>>): Prettify<Theme<SpecificTheme>>;
