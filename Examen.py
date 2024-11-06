class Queue (object):
    def __init__(self,Size):
        self. _maxsize = Size
        self._que = [None] * Size
        self.front = 1
        self._rear = 0
        self._nItems =0
        
    def Insert (self, item):
        if self.isfull():
            raise Exception ("Cola llena")
        self._rear +=1
        if self._rear == self._maxsize:
            self._rear = 0 
        self._que[self._rear] = item
        self._nItems +=1
        return True


    def dequeue(self):
        if not self.is_empty():
            item = self.array.__a[self.front]
            self.front = (self.front + 1) % len(self.array.__a)
            self.array.nItems -= 1
            return item
        return None

    def is_empty(self):
        return self.array.nItems == 0
    
    

        

        
        
        
        