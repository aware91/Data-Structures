"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
        if self.head.next is None:
            self.length = 0
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        value = self.head.value
        self.head = self.head.next
        return value
        #
        # value = self.head.value
        # self.delete(self.head)
        # return value

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
        if self.tail.prev is None:
            self.length = 0
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        value = self.tail.value
        self.tail = self.tail.prev
        return value
        #
        # value = self.tail.value
        # self.delete(self.tail)
        # return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            pass
        else:
            node.next = self.head
            self.head = node
        # if node is self.head:
        #     pass
        # value = node.value
        # self.delete(node)
        # self.add_to_head(value)

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            pass
        value = node.value
        self.delete(node)
        self.add_to_tail(value)


    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.head == None:
            pass
        elif self.head == node:
            self.remove_from_head()
        elif self.tail == node:
            self.remove_from_tail()
        else:
            self.move_to_front(node)
            self.remove_from_head()
            self.head.next = self.tail
        # if not self.head and not self.tail:
        #     return
        # if self.head is self.tail:
        #     self.head = None
        #     self.tail = None
        # elif self.head is node:
        #     self.head = node.next
        #     node.delete()
        # elif self.tail is node:
        #     self.tail = node.prev
        #     node.delete()
        # else:
        #     node.delete()
        # self.length -= 1

    """
    Finds and returns the maximum value of all the nodes
    in the List.
    """
    def get_max(self):
        current_max = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            current = current.next
        return current_max