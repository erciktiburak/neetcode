class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = max(1, capacity)  # Ensure capacity is at least 1
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Cannot pop from an empty array.")
        popped_element = self.array[self.size - 1]
        self.size -= 1
        return popped_element

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


# Example usage:
# Initialize DynamicArray with capacity 1
dynamic_array = DynamicArray(1)

# Push elements and perform operations
dynamic_array.pushback(1)
print(dynamic_array.getSize())       # Output: 1
print(dynamic_array.getCapacity())   # Output: 1

dynamic_array.pushback(2)
print(dynamic_array.getSize())       # Output: 2
print(dynamic_array.getCapacity())   # Output: 2

print(dynamic_array.get(1))          # Output: 2

dynamic_array.set(1, 3)
print(dynamic_array.get(1))          # Output: 3

print(dynamic_array.popback())       # Output: 3
print(dynamic_array.getSize())       # Output: 1
print(dynamic_array.getCapacity())   # Output: 2