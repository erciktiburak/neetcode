class DynamicArray {
    /**
     * @constructor
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = Math.max(1, capacity);
        this.size = 0;
        this.array = new Array(this.capacity).fill(0);
    }

    /**
     * @param {number} i
     * @returns {number}
     */
    get(i) {
        return this.array[i];
    }

    /**
     * @param {number} i
     * @param {number} n
     * @returns {void}
     */
    set(i, n) {
        this.array[i] = n;
    }

    /**
     * @param {number} n
     * @returns {void}
     */
    pushback(n) {
        if (this.size === this.capacity) {
            this.resize();
        }
        this.array[this.size] = n;
        this.size++;
    }

    /**
     * @returns {number}
     */
    popback() {
        if (this.size === 0) {
            throw new Error("Cannot pop from an empty array.");
        }
        const poppedElement = this.array[this.size - 1];
        this.size--;
        return poppedElement;
    }

    /**
     * @returns {void}
     */
    resize() {
        this.capacity *= 2;
        const newArray = new Array(this.capacity);
        for (let i = 0; i < this.size; i++) {
            newArray[i] = this.array[i];
        }
        this.array = newArray;
    }

    /**
     * @returns {number}
     */
    getSize() {
        return this.size;
    }

    /**
     * @returns {number}
     */
    getCapacity() {
        return this.capacity;
    }
}

// Example usage:
// Initialize DynamicArray with capacity 1
const dynamicArray = new DynamicArray(1);

// Push elements and perform operations
dynamicArray.pushback(1);
console.log(dynamicArray.getSize());       // Output: 1
console.log(dynamicArray.getCapacity());   // Output: 1

dynamicArray.pushback(2);
console.log(dynamicArray.getSize());       // Output: 2
console.log(dynamicArray.getCapacity());   // Output: 2

console.log(dynamicArray.get(1));          // Output: 2

dynamicArray.set(1, 3);
console.log(dynamicArray.get(1));          // Output: 3

console.log(dynamicArray.popback());       // Output: 3
console.log(dynamicArray.getSize());       // Output: 1
console.log(dynamicArray.getCapacity());   // Output: 2