import { type InquirerReadline } from '@inquirer/type';
import { type KeypressEvent } from './key.mjs';
export declare function useKeypress(userHandler: (event: KeypressEvent, rl: InquirerReadline) => void | Promise<void>): void;
