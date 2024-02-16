class Node:
    """A class to represent a node in a linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A class to represent a linked list."""

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Print the linked list

        Algorithm:

        1. Start at the head of the linked list
        2. While we have a node
            a. Print the value of the node
            b. Move to the next node

        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """Append a node to the end of the list

        1. Create a new node with the value passed to the function
        2. If the linked list is empty:
            a. Set the head to be the new node
            b. Set the tail to be the new node
        3. If the linked list is not empty:
            a. Set the next property on the tail to be that node
        4. Increment the length by 1
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        """Remove the last node from the linked list

        Algorithm:

        1. If the linked list is empty, return None
        2. Loop through the linked list until you reach the tail
        3. Set the next property of the 2nd to last node to be None
        4. Set the tail to be the 2nd to last node
        5. Decrement the length of the list by 1
        6. Return the node that was popped
        7. If the linked list is empty, set the head and tail to be None
        """
        # if the linked list is empty
        if self.length == 0:
            return None

        # if the linked list contains 2 or more items
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # if the linked list contained 1 item head and tail still are pointing to that node, so, make it None
        if self.length == 0:
            self.head = None
            self.tail = None

        return temp  # return popped item

    def prepend(self, value):
        """Prepend a node to the start of the list

        Algorithm:

        1. Create a new node with the value passed to the function
        2. If the linked list is empty:
            a. Set the head to be the new node
            b. Set the tail to be the new node
        3. If the linked list is not empty:
            a. Set the new node's next node to be the current head
            b. Set the head to be the new node
        4. Increment the length by 1
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        """Remove the first node from the linked list

        Algorithm:

        1. If the linked list is empty, return None
        2. Store the current head in a variable
        3. Set the head to be the current head's next node
        4. Remove the pointer from the old head to the new head
        5. Decrement the length by 1
        6. Return the node that was popped
        7. If the linked list is empty, set the tail to be None
        """
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        """Get the node at the given index

        Algorithm:

        1. If the index is less than zero or greater than or equal to the length of the list, return None
        2. Loop through the list until you reach the index and return the node at that specific index
        """
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """Set the value of the node at the given index

        Algorithm:

        1. Create a variable which is the result of the get method at the index passed to the function
        2. If the get method returns a valid node, set the value of that node to be the value passed to the function and return True
        3. Otherwise, return False
        """
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        """Insert a new node at the given index

        Algorithm:

        1. If the index is less than zero or greater than the length, return False
        2. If the index is the same as the length, use the append method
        3. If the index is 0, use the prepend method

        4. Create a new node with the value passed to the function
        5. Find the node at the index - 1
        6. Set the next property of the new node to be the found node's next property
        7. Set the next property on that found node to be the new node
        8. Increment the length
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True

    def remove(self, index):
        """Remove the node at the given index

        Algorithm:

        1. If the index is less than zero or greater than the length, return None
        2. If the index is the same as the length - 1, use the pop method
        3. If the index is 0, use the pop_first method

        4. Find the node at the index - 1
        5. Set the next property on that node to be the next of the next node
        6. Decrement the length
        7. Return the node that was removed
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp

    def reverse(self):
        """Reverse the linked list

        Algorithm:

        1. Swap the head and tail
        2. Create a variable called next
        3. Create a variable called before

        4. Loop through the list
            a. Set next to be the next property on whatever node is
            b. Set the next property on the node to be whatever before is
            c. Set before to be the value of the node
            d. Set the node to be the value of next"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


if __name__ == "__main__":
    # Create a new Linked List
    ll = LinkedList(1)
    ll.print_list()

    # Append
    ll.append(2)
    ll.print_list()

    # Pop
    popped = ll.pop()
    print("Popped item:", popped.value)
    print("Updated linked list:")
    ll.print_list()

    # Prepend
    value = 5
    print("Prepend", value)
    ll.prepend(value)
    print("Linked List after prepend:")
    ll.print_list()

    # Pop first
    print("Pop first")
    ll.pop_first()
    ll.print_list()

    # Get
    ll.append(54)
    ll.append(109)
    ll.append(6)
    index = 2
    value = ll.get(index)
    print(f"Got value {value.value} on index {index}")

    # Set value
    value = 666
    ll.set_value(index, value)
    print(f"New value of index {index} is {ll.get(index).value}")

    # Insert
    index = 2
    value = 777
    print(f"Insert {value} on index {index}")
    print("Before insert:")
    ll.print_list()
    ll.insert(index, value)
    print("After insert:")
    ll.print_list()

    # Remove
    index = 2
    print(f"Remove value on index {index}")
    print("Before remove:")
    ll.print_list()
    ll.remove(index)
    print("After remove:")
    ll.print_list()

    # Reverse
    print("Before reverse:")
    ll.print_list()
    ll.reverse()
    print("After reverse:")
    ll.print_list()
