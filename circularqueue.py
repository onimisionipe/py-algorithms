#implementing algo for circular queue
"""
please read the doc in queuealgo.py
the usage here is similar. just replace q with c.
that is, instead of q.enqueue(), here you use c.enqueue(), c.dequeue()
"""


class CircularQueue:
    def __init__(self):
        #initialize properties
        self.front = -1;
        self.rear = -1;
        #initialized item to a list
        self.item = [];

    def enqueue(self):
        self.rear = self.rear + 1

        #user input
        rawinput = input("Enter a value:  ");
        print("Value entered");

        if self.front == -1:
            self.front = 0;
            self.rear = 0;

        self.item.insert(0,rawinput);

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty");
            exit();
        else:
            print(self.item.pop());
        if self.rear == self.front:
            self.rear = -1;
            self.front = -1;
        else:
            self.front = self.front + 1;

    def display(self):
        return self.item;


if __name__ == "__main__":
    c = CircularQueue();
    c.enqueue();
            
                
            
        
