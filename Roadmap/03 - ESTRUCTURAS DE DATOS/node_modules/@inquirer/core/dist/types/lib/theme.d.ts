import type { Prettify } from '@inquirer/type';
type DefaultTheme = {
    prefix: string;
    spinner: {
        interval: number;
        frames: string[];
    };
    style: {
        answer: (text: string) => string;
        message: (text: string) => string;
        error: (text: string) => string;
        defaultAnswer: (text: string) => string;
        help: (text: string) => string;
        highlight: (text: string) => string;
        key: (text: string) => string;
    };
};
export type Theme<Extension extends object = object> = Prettify<Extension & DefaultTheme>;
export declare const defaultTheme: DefaultTheme;
export {};
