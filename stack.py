#using python for Stack
"""
Usage:

 - open this file with python idle,
 - press F5
 - you should see a message appear like: please enter a value, enter your value and hit enter
 - to view values entered: type: i.display() and hit enter
 - to enter more values: type: i.enstack() and hit enter
 - to delete or pop out values type i.destack() and hit enter
 - remember i.display() will display the stack.
 


"""

class Stack:
    def __init__(self,size):
        self.item = [];
        
        self.top = -1;
        self.size = size;
     

    #the insert method
    def stackTop(self):
        if self.top >= self.size:
            print("Stack is full, destack stack to add more data");
            exit();
        else:
            #interrupt user to input value
            rawinput = input("Please enter a value:  ");
                        
            #increment stack
            self.top = self.top + 1;

            self.item.append(rawinput);
            print("Data inserted successfully");

    #delete method
    def unStack(self):
        if self.top == -1:
            print("Nothing to delete from, stack is empty");
            exit();
        else:
            self.top = self.top - 1;
            return self.item.pop();

    #display stack
    def display(self):
        return self.item;

if __name__ == "__main__":
    i = Stack(5);
    i.stackTop();
        

            
            
        
        
        
