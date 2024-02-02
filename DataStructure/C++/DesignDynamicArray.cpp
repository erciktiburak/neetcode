#include <iostream>
#include <vector>

class DynamicArray {
public:
    DynamicArray(int capacity) {
        this->capacity = std::max(1, capacity); // Ensure capacity is at least 1
        this->size = 0;
        this->array.resize(this->capacity, 0);
    }

    int get(int i) {
        return this->array[i];
    }

    void set(int i, int n) {
        this->array[i] = n;
    }

    void pushback(int n) {
        if (this->size == this->capacity) {
            resize();
        }
        this->array[this->size] = n;
        this->size++;
    }

    int popback() {
        if (this->size == 0) {
            throw std::out_of_range("Cannot pop from an empty array.");
        }
        int poppedElement = this->array[this->size - 1];
        this->size--;
        return poppedElement;
    }

    void resize() {
        this->capacity *= 2;
        std::vector<int> newArray(this->capacity, 0);
        for (int i = 0; i < this->size; i++) {
            newArray[i] = this->array[i];
        }
        this->array = newArray;
    }

    int getSize() {
        return this->size;
    }

    int getCapacity() {
        return this->capacity;
    }

private:
    int capacity;
    int size;
    std::vector<int> array;
};

int main() {
    // Example usage:
    // Initialize DynamicArray with capacity 1
    DynamicArray dynamicArray(1);

    // Push elements and perform operations
    dynamicArray.pushback(1);
    std::cout << dynamicArray.getSize() << std::endl;       // Output: 1
    std::cout << dynamicArray.getCapacity() << std::endl;   // Output: 1

    dynamicArray.pushback(2);
    std::cout << dynamicArray.getSize() << std::endl;       // Output: 2
    std::cout << dynamicArray.getCapacity() << std::endl;   // Output: 2

    std::cout << dynamicArray.get(1) << std::endl;          // Output: 2

    dynamicArray.set(1, 3);
    std::cout << dynamicArray.get(1) << std::endl;          // Output: 3

    std::cout << dynamicArray.popback() << std::endl;       // Output: 3
    std::cout << dynamicArray.getSize() << std::endl;       // Output: 1
    std::cout << dynamicArray.getCapacity() << std::endl;   // Output: 2

    return 0;
}