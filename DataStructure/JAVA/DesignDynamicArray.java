public class DynamicArray {
    private int capacity;
    private int size;
    private int[] array;

    public DynamicArray(int capacity) {
        this.capacity = Math.max(1, capacity); // Ensure capacity is at least 1
        this.size = 0;
        this.array = new int[this.capacity];
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (this.size == this.capacity) {
            resize();
        }
        this.array[this.size] = n;
        this.size++;
    }

    public int popback() {
        if (this.size == 0) {
            throw new IndexOutOfBoundsException("Cannot pop from an empty array.");
        }
        int poppedElement = this.array[this.size - 1];
        this.size--;
        return poppedElement;
    }

    private void resize() {
        this.capacity *= 2;
        int[] newArray = new int[this.capacity];
        System.arraycopy(this.array, 0, newArray, 0, this.size);
        this.array = newArray;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}

public static void main(String[] args) {
        // Example usage:
        // Initialize DynamicArray with capacity 1
        DynamicArray dynamicArray = new DynamicArray(1);

        // Push elements and perform operations
        dynamicArray.pushback(1);
        System.out.println(dynamicArray.getSize());       // Output: 1
        System.out.println(dynamicArray.getCapacity());   // Output: 1

        dynamicArray.pushback(2);
        System.out.println(dynamicArray.getSize());       // Output: 2
        System.out.println(dynamicArray.getCapacity());   // Output: 2

        System.out.println(dynamicArray.get(1));          // Output: 2

        dynamicArray.set(1, 3);
        System.out.println(dynamicArray.get(1));          // Output: 3

        System.out.println(dynamicArray.popback());       // Output: 3
        System.out.println(dynamicArray.getSize());       // Output: 1
        System.out.println(dynamicArray.getCapacity());   // Output: 2
}