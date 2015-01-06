/*
 * A "multi-stack" implementation, which can divide a single array into
 * a number of stacks. Each sub-stack has its own size and can grow or
 * shrink as the other sub-stacks need space.
 */

public class ArrayMultiStack<T> {

    private static final int DEFAULT_ARRAY_SIZE = 100;

    private T[] array;
    private ArrayStack<T>[] subStacks;

    public ArrayMultiStack(int size, int numSubStacks) {
        int subStackSize = size / numSubStacks;

        this.array = (T[]) new Object[size];
        this.subStacks = new ArrayStack[numSubStacks];

        int i;
        for (i = 0; i < numSubStacks - 1; i++) {
            this.subStacks[i] = new ArrayStack<T>(this.array,
                                                  i * subStackSize,
                                                  (i + 1) * subStackSize);
        }

        /*
         * If the size is not a multiple of numSubStacks, the last
         * sub-stack takes the extra array elements.
         */
        this.subStacks[i] = new ArrayStack<T>(this.array,
                                              i * subStackSize,
                                              size);
    }

    public ArrayMultiStack(int numSubStacks) {
        this(DEFAULT_ARRAY_SIZE, numSubStacks);
    }

    public ArrayStack<T> getStack(int num) {
        return this.subStacks[num];
    }

    public String toString() {
        String s = "";
        for (int i = 0; i < subStacks.length; i++)
            s += this.subStacks[i].toString();
        return s;
    }
}
