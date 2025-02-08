class Array:
    """
    A simple dynamic array implementation.
    Note: Python's list already acts as a dynamic array, but this class
    shows the basic idea with explicit insertion, deletion, and access methods.
    """
    def __init__(self):
        # Initialize an empty list to store elements
        self.data = []
    
    def insert(self, index, value):
        """
        Insert value at the specified index.
        If index is out of bounds, append at the end.
        """
        if index < 0 or index > len(self.data):
            # If the index is invalid, append at the end.
            self.data.append(value)
        else:
            self.data.insert(index, value)
    
    def delete(self, index):
        """
        Delete element at the specified index.
        Raises IndexError if index is invalid.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data.pop(index)
    
    def access(self, index):
        """
        Return the element at the given index.
        Raises IndexError if index is invalid.
        """
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of range")
        return self.data[index]
    
    def __str__(self):
        return str(self.data)

# Example usage of Array
print("---- Array Example ----")
arr = Array()
arr.insert(0, 10)   # Insert 10 at index 0
arr.insert(1, 20)   # Insert 20 at index 1
arr.insert(1, 15)   # Insert 15 at index 1, pushing 20 to the right
print("Array after insertions:", arr)  # Expected: [10, 15, 20]
print("Element at index 1:", arr.access(1))  # Expected: 15
removed = arr.delete(1)  # Remove the element at index 1
print("Removed element:", removed)  # Expected: 15
print("Array after deletion:", arr)  # Expected: [10, 20]

print("\n")

class Matrix:
    """
    A simple Matrix implementation using a list of lists.
    Supports access, update, insertion and deletion of rows.
    """
    def __init__(self, rows, cols, default=0):
        # Initialize a matrix with given number of rows and columns.
        # All elements are initialized to the default value.
        self.rows = rows
        self.cols = cols
        self.data = [[default for _ in range(cols)] for _ in range(rows)]
    
    def get(self, row, col):
        """
        Return the value at (row, col).
        """
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        return self.data[row][col]
    
    def set(self, row, col, value):
        """
        Set the value at (row, col) to 'value'.
        """
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of range")
        self.data[row][col] = value
    
    def insert_row(self, index, row_data=None):
        """
        Insert a new row at the specified index.
        If row_data is None, a row with default values (0) is inserted.
        """
        if row_data is None:
            row_data = [0 for _ in range(self.cols)]
        elif len(row_data) != self.cols:
            raise ValueError("Row length must match number of columns")
        if index < 0 or index > self.rows:
            raise IndexError("Index out of range")
        self.data.insert(index, row_data)
        self.rows += 1
    
    def delete_row(self, index):
        """
        Delete the row at the specified index.
        """
        if index < 0 or index >= self.rows:
            raise IndexError("Index out of range")
        self.data.pop(index)
        self.rows -= 1
    
    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += str(row) + "\n"
        return matrix_str

# Example usage of Matrix
print("---- Matrix Example ----")
mat = Matrix(2, 3)  # Create a 2x3 matrix initialized with zeros
print("Initial matrix:")
print(mat)
mat.set(0, 1, 5)    # Set element at row 0, col 1 to 5
mat.set(1, 2, 10)   # Set element at row 1, col 2 to 10
print("Matrix after updates:")
print(mat)
mat.insert_row(1, [7, 8, 9])  # Insert a new row at index 1
print("Matrix after inserting a row at index 1:")
print(mat)
mat.delete_row(0)   # Delete the first row
print("Matrix after deleting the first row:")
print(mat)

print("\n")

class Stack:
    """
    A simple stack implementation using a Python list.
    Supports push, pop, and peek operations.
    """
    def __init__(self):
        self.data = []
    
    def push(self, value):
        """
        Push a value onto the stack.
        """
        self.data.append(value)
    
    def pop(self):
        """
        Pop a value from the top of the stack.
        Raises IndexError if the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.data.pop()
    
    def peek(self):
        """
        Return the top element without removing it.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.data[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.data) == 0
    
    def __str__(self):
        return str(self.data)

# Example usage of Stack
print("---- Stack Example ----")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack after pushes:", stack)  # Expected: [1, 2, 3]
print("Top element:", stack.peek())    # Expected: 3
print("Popped element:", stack.pop())    # Expected: 3
print("Stack after pop:", stack)         # Expected: [1, 2]

print("\n")

class Queue:
    """
    A simple queue implementation using a Python list.
    Supports enqueue and dequeue operations.
    """
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        """
        Add a value to the end of the queue.
        """
        self.data.append(value)
    
    def dequeue(self):
        """
        Remove and return the value at the front of the queue.
        Raises IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.data.pop(0)  # pop the first element
    
    def peek(self):
        """
        Return the value at the front without removing it.
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.data[0]
    
    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return len(self.data) == 0
    
    def __str__(self):
        return str(self.data)

# Example usage of Queue
print("---- Queue Example ----")
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print("Queue after enqueues:", queue)   # Expected: ['A', 'B', 'C']
print("Front element:", queue.peek())     # Expected: 'A'
print("Dequeued element:", queue.dequeue())  # Expected: 'A'
print("Queue after dequeue:", queue)       # Expected: ['B', 'C']

print("\n")

class ListNode:
    """
    A node in a singly linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node

class LinkedList:
    """
    A simple singly linked list implementation.
    Supports insertion, deletion, and traversal.
    """
    def __init__(self):
        self.head = None  # Start of the list
    
    def insert_at_beginning(self, value):
        """
        Insert a new node at the beginning of the list.
        """
        new_node = ListNode(value)
        new_node.next = self.head  # Link new node to current head
        self.head = new_node       # Update head to new node
    
    def insert_at_end(self, value):
        """
        Insert a new node at the end of the list.
        """
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return
        # Traverse to the end of the list
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_value(self, value):
        """
        Delete the first occurrence of the value in the list.
        Returns True if deletion was successful, False otherwise.
        """
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    # Deleting the head
                    self.head = current.next
                else:
                    previous.next = current.next
                return True  # Value found and deleted
            previous = current
            current = current.next
        return False  # Value not found
    
    def traverse(self):
        """
        Traverse the list and return a list of node values.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def __str__(self):
        return " -> ".join(str(val) for val in self.traverse())

# Example usage of LinkedList
print("---- Linked List Example ----")
ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_end(15)
print("Linked List after insertions:", ll)  # Expected: 5 -> 10 -> 15
ll.delete_value(10)
print("Linked List after deleting 10:", ll)  # Expected: 5 -> 15
print("Traversal output:", ll.traverse())    # Expected list: [5, 15]

print("\n")

class TreeNode:
    """
    A node in a rooted tree.
    Each node has a value and a list of children.
    """
    def __init__(self, value):
        self.value = value
        self.children = []  # List to store child nodes
    
    def add_child(self, child_node):
        """
        Add a child node.
        """
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        """
        Remove a child node.
        """
        self.children = [child for child in self.children if child != child_node]
    
    def __str__(self, level=0):
        """
        Return a string representation of the tree for visualization.
        """
        ret = " " * (level * 4) + f"- {self.value}\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

# Example usage of Rooted Tree
print("---- Rooted Tree Example ----")
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")
child3 = TreeNode("Child 3")
subchild1 = TreeNode("Subchild 1")
subchild2 = TreeNode("Subchild 2")

# Build the tree
root.add_child(child1)
root.add_child(child2)
child2.add_child(subchild1)
child2.add_child(subchild2)
root.add_child(child3)

print("Tree structure:")
print(root)
