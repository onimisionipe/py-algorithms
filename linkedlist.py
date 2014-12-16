"""
Start the program by hitting the F5 key. this brings up ine interactive intepreter
to insert a node at the begining, you type li.insertBegining("what i want to insert");
to insert at the end, you type li.insertEnd("what i want to insert");
to search, you type li.search("what i am searching for")
to display, you type li.display(), this displays nodes and the next node, that is what they are linked to
    
"""


class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None;
        

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext;


class LinkedList:

    def __init__(self):
        self.head = None;
        self.tail = None;

    """
    This method checks if list is empty and returns boolean
    """
    def isEmpty(self):
        return self.head == None;

    def insertBegining(self,item):
        temp = Node(item);
        temp.setNext(self.head);
        #if list is empty, set tail to node
        if self.isEmpty() == True:
            self.tail = temp;
            
        self.head = temp;

    def insertEnd(self,item):
        temp = Node(item);
        if self.isEmpty() != True:
            self.tail.setNext(temp);
            self.tail = temp;
        

    
    def search(self,item):
        current = self.head;
        found = False;
        while current != None and not found:
            if current.getData() == item:
                found = True;
            else:
                current = current.getNext();
        return found;

    def display(self):
        current = self.head;
        while current != None:
            print(current.getData());
            print("------------>"+current.getNext().getData()) if current.getNext() != None else print("---------->None");
            current = current.getNext();
        
        

    #This can be skipped as it is not part of the assignment. this is used for deleting nodes from the list
    def remove(self,item):
        current = self.head;
        previous = None;
        found = False;
        while not found:
            if current.getData() == item:
                found = True;
            else:
                previous = current;
                current = current.getNext();

        if previous == None:
            self.head = current.getNext();

        else:
            previous.setNext(current.getNext());

if __name__ == "__main__":
    li = LinkedList();
    
        



    
    
