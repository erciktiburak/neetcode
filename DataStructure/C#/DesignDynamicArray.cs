using System;

public class DynamicArray {
    private int capacity;
    private int size;
    private int[] array;

    public DynamicArray(int capacity) {
        this.capacity = Math.Max(1, capacity); // Ensure capacity is at least 1
        this.size = 0;
        this.array = new int[this.capacity];
    }

    public int Get(int i) {
        return this.array[i];
    }

    public void Set(int i, int n) {
        this.array[i] = n;
    }

    public void PushBack(int n) {
        if (this.size == this.capacity) {
            Resize();
        }
        this.array[this.size] = n;
        this.size++;
    }

    public int PopBack() {
        if (this.size == 0) {
            throw new InvalidOperationException("Cannot pop from an empty array.");
        }
        int poppedElement = this.array[this.size - 1];
        this.size--;
        return poppedElement;
    }

    private void Resize() {
        this.capacity *= 2;
        int[] newArray = new int[this.capacity];
        Array.Copy(this.array, newArray, this.size);
        this.array = newArray;
    }

    public int GetSize() {
        return this.size;
    }

    public int GetCapacity() {
        return this.capacity;
    }

    public static void Main() {
        // Example usage:
        // Initialize DynamicArray with capacity 1
        DynamicArray dynamicArray = new DynamicArray(1);

        // Push elements and perform operations
        dynamicArray.PushBack(1);
        Console.WriteLine(dynamicArray.GetSize());       // Output: 1
        Console.WriteLine(dynamicArray.GetCapacity());   // Output: 1

        dynamicArray.PushBack(2);
        Console.WriteLine(dynamicArray.GetSize());       // Output: 2
        Console.WriteLine(dynamicArray.GetCapacity());   // Output: 2

        Console.WriteLine(dynamicArray.Get(1));          // Output: 2

        dynamicArray.Set(1, 3);
        Console.WriteLine(dynamicArray.Get(1));          // Output: 3

        Console.WriteLine(dynamicArray.PopBack());       // Output: 3
        Console.WriteLine(dynamicArray.GetSize());       // Output: 1
        Console.WriteLine(dynamicArray.GetCapacity());   // Output: 2
    }
}