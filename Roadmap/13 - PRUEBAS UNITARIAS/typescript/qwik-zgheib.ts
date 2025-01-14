import assert from "assert";

export const sum = (a: number, b: number): number => a + b;

function test(description: string, fn: () => void): void {
  try {
    fn();
    console.log(`✔️  ${description}`);
  } catch (error) {
    console.log(`❌  ${description}`);
    console.error(error);
  }
}

test("adds 1 + 2 to equal 3", () => {
  assert.strictEqual(sum(1, 2), 3);
});

test("adds 1 + 1 to equal 2", () => {
  assert.strictEqual(sum(1, 1), 2);
});
