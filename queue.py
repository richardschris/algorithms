class Queue:
    class _Node:
        # The linked list implementation...
        def __init__(self, value=None):
            self.child = None
            self.value = value

        def add_child(self, value):
            self.child = self.__class__(value)
            return self.child

    def __init__(self):
        self.queue = self._Node()
        self.end = self.queue

    def add(self, item):
        if self.queue.value:
            child = self.end.add_child(item)
            self.end = child
        else:
            self.queue.value = item
        return self

    def remove(self):
        value = self.queue.value
        self.queue = self.queue.child if self.queue.child else self._Node()
        return value

    def peek(self):
        return self.queue.value
