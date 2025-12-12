"""A queue made with a linked list"""
class QueueLink:

    """Creates a node object and creates the linked list of nodes as well"""
    def __init__(self, list_links : str):

        #the current head of the queue 
        self.head:Node = None

        #sets the tail node, the final entry, useful to have if we want to extend the number of items
        #onto the queue
        self.tail:Node = None

        #creates a linked list out of nodes
        self.add_links(list_links)

    """Tests a traversal of all elements by going through them"""
    def test_traverse(self) -> None:
        self.head_preserved = self.head
        while self.head:
            print(self.head.get_val())
            self.head=self.head.get_next()
        
        self.head = self.head_preserved

    """Add links to the queue"""
    def add_links(self, list_links:str):
        
        new  = self.head
        if self.tail:
            new = self.tail

        #creates a linked list out of nodes
        for link in list_links:

            #if there is a head node process normally 
            if self.head:
                new_node : Node = Node(link,None)

                #set the current node's next node to the node just created
                new.set_next(new_node)
                new = new_node
            
            #if there isn't a head node, then create one
            else:
                self.head = Node(link,None) 
                new = self.head
            
            self.tail = new 
        
        #show that new entries were actually added
        #self.test_traverse()

    """Returns the item of the next node without changing the value of the head node"""
    def peek(self) -> str:
        if self.head.next:
            return self.head.next
        else:
            return None
    
    """Moves the pointer up by one"""
    def advance_node(self) -> None:
        self.head=self.head.next

    #getters
    """Returns the tail node"""
    def get_tail(self):
        return self.tail
    
    """Returns the head node"""
    def get_head(self):
        return self.head



"""Each member of the link queue linked list"""
class Node:
    #the val at this instance 
    val : str 

    """Sets the val and next element"""
    def __init__(self, val  : str, next):
        self.val = val
        self.next = next 

    #Setters
    """Sets the value to a new value"""
    def set_val(self, new_val) -> None:
        self.val = new_val

    """Sets the value of the next node"""
    def set_next(self, next_node) -> None:
        self.next = next_node

    #Getters 
    def get_val(self) -> None:
        return self.val
    
    #Returns the next value  
    def get_next(self):
        return self.next