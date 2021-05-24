class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.prev = prev  # for double linkedlist
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head.data == None:
            self.head = new_node
            return
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def insert(self, data, pos=0):
        '''
        insert function use to insert node to pos th place of linkedlist
        '''
        new_node = Node(data)
        if pos > self.length():
            self.append(data)
        elif pos == 0:
            self.push(data)
        else:
            # head -> 1  -> 2 -> 3 -> 4 -> 5 -> 6
            # traversal to pos
            prev = self.head
            after = self.head.next
            for _ in range(pos - 1):
                prev = prev.next
                after = after.next
            prev.next = new_node
            new_node.next = after

    def push(self, data):
        '''
        push function use to push node in 1st place of linkedlist
        '''
        new_node = Node(data)
        if self.head.data == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete_all(self):
        # initialize the current node
        current = self.head
        while current:
            prev = current.next  # move next node
            # delete the current node
            del current.data
            # set current equals prev node
            current = prev

    def delete_node(self, key=None, position=None):
        # position start from 0 for the head
        if key is not None:
            # Store head node
            temp = self.head
            # If head node itself holds the key to be deleted
            if temp:
                if (temp.data == key):
                    self.head = temp.next
                    temp = None
                    return

            # Search for the key to be deleted, keep track of the
            # previous node as we need to change 'prev.next'
            while(temp is not None):
                if temp.data == key:
                    break
                prev = temp
                temp = temp.next

            # if key was not present in linked list
            if (temp == None):
                print('not found')
                return None
            #  if found prev = temp, temp->temp.next , prev.data = key
            # Unlink the node from linked list
            prev.next = temp.next
            temp = None
        if position is not None:
            # position became the pos of prev node to delete the node after
            # If linked list is empty
            if self.head == None:
                return
            # Store head node
            temp = self.head
            # If head needs to be removed
            if position == 0:
                self.head = temp.next
                temp = None
                return

            # Find previous node of the node to be deleted
            for _ in range(position - 1):
                temp = temp.next
                if temp is None:
                    break
            # If position is more than number of nodes
            if temp is None:
                return
            if temp.next is None:
                return
            # Node temp.next is the node to be deleted
            # store pointer to the next of node to be deleted
            next = temp.next.next
            # Unlink the node from linked list
            temp.next = None
            temp.next = next

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def length_rec(self, node):
        if not node:
            return 0
        else:
            return 1 + self.length_rec(node.next)

    def print_LinkedList(self):
        temp = self.head
        ll_str = ''
        while temp != None:
            ll_str += (str(temp.data))
            temp = temp.next
            if temp != None:
                ll_str += ' -> '
        print('head ->', ll_str)

    def get_node(self, pos=0):
        c = 0
        curr = self.head
        while curr:
            if c == pos:
                return curr.data
            curr = curr.next
            c += 1
        return None

    def index(self, data) -> int:
        index = 0
        curr = self.head
        while curr:
            if curr.data == data:
                return index
            curr = curr.next
            index += 1
        return None

    def removeDuplicates(self):
        prev = self.head
        cur = self.head
        while cur.next:
            cur = cur.next
            if prev.data == cur.data:
                prev.next = cur.next
            else:
                prev = prev.next
        return self.head


if __name__ == '__main__':
    # empty list:
    llist = LinkedList()
    llist.head = Node()
    # push value
    # for i in range(1, 10):
    #     llist.push(i)
    # append value
    # for i in range(10):
    #     llist.append(i ** 2)
    # llist.insert(data='end', pos=100)
    l = [1, 1, 2, 3, 3, 4, 5, 5]
    for x in l:
        llist.append(x)
    print(f'Length of linked list is: {llist.length()}\n>>>LinkedList:')
    llist.print_LinkedList()
    llist.removeDuplicates()
    llist.print_LinkedList()
