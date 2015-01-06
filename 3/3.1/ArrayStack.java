/*
 * A stack implementation based on an array. ArrayStacks are used by
 * the ArrayMultiStack class to define regions of a single array to
 * use as sub-stacks. This stack class can take a reference to an array
 * with start and ending indices, or it can allocate its own array.
 */

public class ArrayStack<T> {
    private static final int DEFAULT_INITIAL_SIZE = 10;

    private T[] array;
    private int start;
    private int end;

    private int next;

    // note: start is inclusive, end is exclusive
    public ArrayStack(T[] arr, int start, int end) {
        if (start > end)
            throw new IllegalArgumentException();

        if (arr == null)
            throw new IllegalArgumentException();

        this.array = arr;
        this.start = start;
        this.end = end;

        this.next = start;
    }

    public ArrayStack(int size) {
        this((T[])new Object[size], 0, size);
    }

    public ArrayStack() {
        this(DEFAULT_INITIAL_SIZE);
    }

    public int size() {
        return next - start;
    }

    public void add(T item) throws StackOverflowException {
        if (next + 1 > end)
            throw new StackOverflowException();

        this.array[next++] = item;
    }

    public void resize(int newStart, int newEnd)
        throws InsufficientSpaceException
    {
        if (newStart > newEnd)
            throw new IllegalArgumentException();

        int numItems = size();
        int newSize = newStart - newEnd;
        int shiftAmount = Math.abs(newStart - this.start);

        if (newSize < numItems)
            throw new InsufficientSpaceException();

        for (int i = newStart + numItems; i >= newStart; i--)
            this.array[i] = this.array[i - shiftAmount];

        this.start = newStart;
        this.end = newEnd;
        this.next = newStart + numItems;
    }

    public String toString() {
        int numItems = size();
        String s = "[";

        if (numItems >= 1)
            s += this.array[start].toString();

        for (int i = start + 1; i < next; i++)
            s += ", " + this.array[i].toString();

        return s + "]";
    }

    public static void main(String[] args) {
        ArrayStack<String> s = new ArrayStack<String>(1);
        System.out.println(s);

        try {
            s.add("Hello!");
        } catch (StackOverflowException e) {
            System.exit(1);
        }

        System.out.println(s);

        try {
            s.add("Oops!");
        } catch (StackOverflowException e) {
            System.err.println("Stack overflow!");
        }
    }
}

class InsufficientSpaceException extends Exception { }
class StackOverflowException extends Exception { }
