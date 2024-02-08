class Node {
    constructor(val) {
        this.data = val;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if (index < 0 || this.head === null)
            return -1;

        let current = this.head;
        let count = 0;
        while (current !== null && count < index) {
            current = current.next;
            count++;
        }
        if (current !== null)
            return current.data;
        else
            return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        let newNode = new Node(val);
        newNode.next = this.head;
        this.head = newNode;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        let newNode = new Node(val);
        if (this.head === null) {
            this.head = newNode;
            return;
        }

        let current = this.head;
        while (current.next !== null) {
            current = current.next;
        }
        current.next = newNode;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        if (index < 0 || this.head === null)
            return false;

        if (index === 0) {
            this.head = this.head.next;
            return true;
        }

        let current = this.head;
        let count = 0;
        while (current !== null && count < index - 1) {
            current = current.next;
            count++;
        }

        if (current === null || current.next === null)
            return false;

        current.next = current.next.next;
        return true;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        let values = [];
        let current = this.head;
        while (current !== null) {
            values.push(current.data);
            current = current.next;
        }
        return values;
    }
}

// Example usage:
let list = new LinkedList();
list.insertHead(1);
list.insertTail(2);
list.insertHead(0);
list.remove(1);
console.log(list.getValues()); // Output: [0, 2]
