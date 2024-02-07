#include <vector>
using namespace std;

// Node class for the linked list
class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
private:
    Node* head; // Pointer to the head of the linked list

public:
    // Constructor to initialize an empty linked list
    LinkedList() : head(nullptr) {}

    // Function to get the value of the ith node (0-indexed)
    // Returns -1 if index is out of bounds
    int get(int index) {
        if (index < 0)
            return -1;

        Node* current = head;
        int count = 0;
        while (current != nullptr && count < index) {
            current = current->next;
            count++;
        }
        if (current != nullptr)
            return current->data;
        else
            return -1;
    }

    // Function to insert a node with value val at the head of the list
    void insertHead(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }
    
    // Function to insert a node with value val at the tail of the list
    void insertTail(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
            return;
        }

        Node* current = head;
        while (current->next != nullptr) {
            current = current->next;
        }
        current->next = newNode;
    }

    // Function to remove the ith node (0-indexed)
    // Returns false if index is out of bounds, otherwise returns true
    bool remove(int index) {
        if (index < 0)
            return false;
        
        if (index == 0) {
            if (head != nullptr) {
                Node* temp = head;
                head = head->next;
                delete temp;
                return true;
            } else {
                return false;
            }
        }

        Node* current = head;
        int count = 0;
        while (current != nullptr && count < index - 1) {
            current = current->next;
            count++;
        }

        if (current == nullptr || current->next == nullptr)
            return false;

        Node* temp = current->next;
        current->next = temp->next;
        delete temp;
        return true;
    }

    // Function to return an array of all the values in the linked list, ordered from head to tail
    vector<int> getValues() {
        vector<int> values;
        Node* current = head;
        while (current != nullptr) {
            values.push_back(current->data);
            current = current->next;
        }
        return values;
    }
};