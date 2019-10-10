class l_list:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link
    
    def __init__(self):
        self.head = None
        self.size = 0

    # def size(self):
    #     return self.size

    ## check empty
    def is_empty(self):
        return self.size==0

    ## add node at front
    def add_node_front(self, item):
        if(self.is_empty()):
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    ## add node at specific location(next to node p)
    def add_node(self, item, value):
        if(self.is_empty()):
            print("Not exist {}".format(value))
        else:
            p = self.head
            while(p):
                if(p.item == item):
                    break
                else:
                    p = p.next
            if(p.next == None):
                p.next = self.Node(value, None)
            else:
                p.next = self.Node(value, p.next)
            self.size += 1

    ## delete node at front
    def del_node_front(self):
        if(self.is_empty()):
            print("Empty list!")
        else:
            self.head = self.head.next
            self.size -= 1

    ## delete node at specific location(next to node p)
    def del_node(self, value):
        if(self.is_empty()):
            print("Empty list!")
        else:
            p = self.head
            while(p):
                if(p.item != value):
                    q = p
                    p = p.next
                else:
                    q.next = p.next
                    self.size -= 1
                    break
                    
    ## search node
    def search_node(self, value):
        if(self.is_empty()):
            print("Empty list!")
        else:
            p = self.head
            idx = 0
            while(p):
                if(p.item == value):
                    return idx
                else:
                    p = p.next
                    idx += 1

    ## print list
    def print_list(self):
        p = self.head
        while(p):
            if(p.next!=None):
                print("{} -> ".format(p.item), end="")
            else:
                print("{}".format(p.item))
            p = p.next

def main():
    l = l_list()
    l.add_node_front(3)
    l.add_node_front(5)
    l.add_node_front(7)
    l.print_list()

    # l.del_node_front()
    # l.print_list()
    # l.del_node_front()
    # l.print_list()

    l.add_node(5, 8)
    l.print_list()

    l.del_node(5)
    l.print_list()

    l_head = l.head
    while(l_head):
        print("{} is {}'s node!".format(l_head.item, l.search_node(l_head.item)))
        l_head = l_head.next

if(__name__ == '__main__'):
    main()