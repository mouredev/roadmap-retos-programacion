import type { InquirerReadline } from '@inquirer/type';
export default class ScreenManager {
    private readonly rl;
    private height;
    private extraLinesUnderPrompt;
    private cursorPos;
    constructor(rl: InquirerReadline);
    write(content: string): void;
    render(content: string, bottomContent?: string): void;
    checkCursorPos(): void;
    done({ clearContent }: {
        clearContent: boolean;
    }): void;
}
