class Door:
    def __init__(self, closed, locked):
        self.closed = closed
        self.lock = locked



    def open(self):
        if self.closed:
            self.closed = False
        else:
            print("Its aready open")

    def close(self):
        if self.closed:
            print("it is already closed")
        else:
            self.closed = True

    def lock(self):
        if self.locked:
            print("it is already locked")
        else:
            self.locked = True
        if self.locked:
            self.locked= False
        else:
            print("Its already unlock")








