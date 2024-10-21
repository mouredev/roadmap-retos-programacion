type NotFunction<T> = T extends Function ? never : T;
export declare function useState<Value>(defaultValue: NotFunction<Value> | (() => Value)): [Value, (newValue: Value) => void];
export declare function useState<Value>(defaultValue?: NotFunction<Value> | (() => Value)): [Value | undefined, (newValue?: Value | undefined) => void];
export {};
