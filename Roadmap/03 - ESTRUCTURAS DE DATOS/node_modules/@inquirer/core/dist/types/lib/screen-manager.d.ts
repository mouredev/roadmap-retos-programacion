import type { InquirerReadline } from '@inquirer/type';
export default class ScreenManager {
    private readonly rl;
    private height;
    private extraLinesUnderPrompt;
    private cursorPos;
    constructor(rl: InquirerReadline);
    render(content: string, bottomContent?: string): void;
    checkCursorPos(): void;
    clean(): void;
    clearContent(): void;
    done(): void;
}
