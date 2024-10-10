import type { InquirerReadline } from '@inquirer/type';
type HookStore = {
    rl: InquirerReadline;
    hooks: any[];
    hooksCleanup: Array<void | (() => void)>;
    hooksEffect: Array<() => void>;
    index: number;
    handleChange: () => void;
};
export declare function withHooks(rl: InquirerReadline, cb: (store: HookStore) => void): void;
export declare function readline(): InquirerReadline;
export declare function withUpdates<T extends (...args: any) => any>(fn: T): (...args: Parameters<T>) => ReturnType<T>;
type SetPointer<Value> = {
    get(): Value;
    set(value: Value): void;
    initialized: true;
};
type UnsetPointer<Value> = {
    get(): void;
    set(value: Value): void;
    initialized: false;
};
type Pointer<Value> = SetPointer<Value> | UnsetPointer<Value>;
export declare function withPointer<Value, ReturnValue>(cb: (pointer: Pointer<Value>) => ReturnValue): ReturnValue;
export declare function handleChange(): void;
export declare const effectScheduler: {
    queue(cb: (readline: InquirerReadline) => void): void;
    run(): void;
};
export {};
