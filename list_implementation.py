class Node:

    def __init__(self, initval=None):
        self.value = initval
        self.next = None

    def is_empty(self):
        return self.value == None

    # appending value to a list
    def appendr(self, v):
        if self.is_empty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.appendr(v)

        return()

    def appendi(self, v):
        if self.is_empty():
            self.value = v

        temp = self
        while temp.next != None:
            temp = temp.next

            newnode = Node(v)
            temp.next = newnode
        return()

    def insert(self, v):
        if self.is_empty():
            self.value = v
            return()

        newnode = Node(v)
        self.value, newnode.value = newnode.value, self.value
        self.next, newnode.next = newnode, self.next
        return()

    def deletei(self, v):
        if self.is_empty():
            return()
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next

        temp = self
        while temp.next != None:
            if temp.next.value == v:
                temp.next = temp.next.next
                return()
            else:
                temp = temp.next
        return()

    def deleter(self, v):
        if self.is_empty():
            return()
        if self.value == v:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
        else:   # recursively delete
            if self.next != None:
                self.next.deleter(v)
                if self.next.value == None:
                    self.next = None
        return()

    def __str__(self):
        selflist = []

        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        return str(selflist)


l = Node(0)
print(l)

for i in range(1, 10):
    l.appendr(i)
print(l)

l.insert(12)
print(l)

l.deletei(4)
print(l)
