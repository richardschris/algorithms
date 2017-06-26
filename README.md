# Algorithms

This is a set of Python implementations of some basic algorithms, for my edification.

## HashMap

HashMap implements a hash table. It is a baby version of a Python dictionary, without the iterator power.

```
>>> from hashmap import HashMap
>>> hash_table = HashMap()

>>> hash_table['hello'] = 'world'
>>> hash_table['hello']
'world'
>>> hash_table.size
1024
>>> hash_table.map
[None, None, None, ..., [('hello', 'world')], ...]
```

HashMap implements a simple hash table using Python's built-in `hash` function. A default  size is set (in this case, 1024), and populated with None objects. When an item is added to the table, it first checks if there is anything at that key by accessing the index at `hash(key) % 1024`. If it's `None`, then it adds a list containing a single tuple (key, value). This prevents against collisions. If there is a collision, then the algorithm adds the new tuple to the list.

To access a key, the key is hashed in the same way as above, and the list retrieved. The list is then searched for the tuple with the right key, and if it exists, the value is returned.

If the list fills up, the algorithm increases the list size. To do this, it has to recreate the whole table from scratch, so things may be distributed in new places. We iterate through the whole hash table, then through each of the individual collision-avoidance lists, rebuilding the hash table from this using the new size.

## Queue

A simple FIFO queue using a linked list.

```
>>> from queue import Queue
>>> q = Queue()
>>> q.add('hi')
>>> q.peek()
'hi'
>>> q.add('another')
>>> q.add('even more')
>>> q.peek()
'hi'
>>> q.remove()
'hi'
>>> q.peek()
'another'
>>> q.remove()
'another'
>>> q.remove()
'even more'
>>> q.peek()
None
```

When we create the queue, we also create a `_Node` which has a child and a value property. The child and value properties are set to `None` on instantiation. When we add a value, we do two things. We first check if there is no child; if there is no child, it means there is only one node, and we can just add the value to that and be done. If there is a child, we don't traverse the list. Rather, we get the end node, add a new child, set the value to the desired one, and then set the end node reference to the new child.

## Binary Search Tree

The binary search tree implementation is very simple. It implements a binary tree, and an order function, to print the values in order.

```
>>> from binarysearch import Node
>>> node = Node(10)
>>> node.add(5)
>>> node.add(2)
>>> node.add(3)
>>> node.add(4)
>>> node.add(20)
>>> node.add(10)
>>> node.add(30)
>>> node.add(15)
>>> node.find(10)
True
>>> node.find(27)
False
>>> node.order()
2
3
4
5
10
15
20
30
```

The algorithm implements nodes with parents and left/right children. Parents are unused but can be used to implement backtracking and upwards traversal. When a value is added, we check if it's greater or less than the current value; if it's greater, then we add a value to the right child. If it's less, we add a value to the left child. This process repeats until it finds an empty node and adds it there. The `find` function takes a value and tells us if it's in the tree. The `order` function returns the tree from lowest to highest.