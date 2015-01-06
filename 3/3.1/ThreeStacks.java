/* 3.1: Describe how you could use a single array to implement three stacks.
 *
 * A simple solution would be to split the array into three even components.
 * If it is acceptable for the three stacks to have a fixed maximum capacity,
 * and all three stacks require the same maximum capacity, this approach
 * would work fine.
 *
 * If the capacities are known beforehand, this is also ideal: the array can
 * be split into three uneven components.
 *
 * However, if the array memory itself is large and fixed, but it must be
 * possible for one stack to use the entire memory space if the other two
 * stacks are empty, some resizing logic is needed.
 *
 * The simplest solution to the resizing stacks is to grow a sub-stack
 * by one position if another position is needed and an adjacent stack
 * has space. This might involve shifting the items in an adjacent stack.
 */

public class ThreeStacks {
    public static void main(String[] args) {
        ArrayMultiStack<String> stacks = new ArrayMultiStack<String>(3);
        ArrayStack<String> s0 = stacks.getStack(0);
        ArrayStack<String> s1 = stacks.getStack(1);
        ArrayStack<String> s2 = stacks.getStack(2);

        try {
            s0.add("Hello!");
            s1.add("Hi!");
            s2.add("Hey!");
        } catch (StackOverflowException e) {

        }

        System.out.println(stacks);
    }
}
