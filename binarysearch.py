class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.lchild = None
        self.rchild = None

    def add(self, value):
        if self.value == value:
            return

        if value > self.value:
            if self.rchild is None:
                self.rchild = self.__class__(value, parent=self)
            else:
                self.rchild.add(value)
        else:
            if self.lchild is None:
                self.lchild = self.__class__(value, parent=self)
            else:
                self.lchild.add(value)

    def find(self, value):
        if self.value == value:
            return True

        if value > self.value:
            if self.rchild is None:
                return False

            return self.rchild.find(value)

        else:
            if self.lchild is None:
                return False

            return self.lchild.find(value)

    def order(self):
        if self.lchild:
            self.lchild.order()
        if self.value:
            print(self.value)
        if self.rchild:
            self.rchild.order() 
