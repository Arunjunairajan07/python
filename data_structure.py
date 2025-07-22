#Big O Notation 
#Time complexity 
# o(1) = constant(print("hi"))
# o(n) = linear (one loop statement )
# o(log n) =  logarithmically (Binary search)
# o(nlog n)= linear  logarithmically
# o(n^2) = quadratically (two or more statement) 

# linear search 
# arr=[2,6,1,7,8,5,9,3]
# for i in range(0,len(arr)):
#     if arr[i]==3:
#         print(i)
#         # or
# n=0
# arr=[1,2,3,6,8,5]
# for i in arr:
#     if i != 5:
#         n=n+1
#     else:
#         break
# print("index value for 5:",n)

# # Binary Search 
arr = [1, 3, 5, 7, 9, 11, 13]
target = 11
low = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(mid)
        break 
    elif arr[mid] < target:
        low = mid + 1  
    else:
        high = mid - 1  
else:   
    print("-1") 

# # recursion 
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# # BUBBLE SORT 
# arr = [64, 25, 12, 22, 11]
# for i in range(0,len(arr)-1):  
#   for j in range(0,len(arr)-1): 
#     if arr[j]<arr[j+1]:
#       continue
#     elif arr[j] > arr[j + 1]:
#       temp = arr[j]
#       arr[j] = arr[j+1]
#       arr[j+1] = temp
# print("Sorted array:  ", arr)
#             # or 
# # Bubble Sort using while loop
# def bubble_sort(arr):
#     n = len(arr)
#     i = 0
#     while i < n:
#         for j in range(0,len(arr)-1):
#             if arr[j] > arr[j + 1]:
#                 temp = arr[j]
#                 arr[j] = arr[j+1]
#                 arr[j+1] = temp
#         i += 1
# arr = [64, 25, 12, 22, 11]
# print("Original array:", arr)
# bubble_sort(arr)
# print("Sorted array:  ", arr)

# Selection Sort
def selection_sort(arr):
    for i in range(0,len(arr)):
        min_index = i  
        for j in range(i+1 , len(arr)):
            if arr[j]< arr[min_index]:
                min_index = j  
        # arr[i], arr[min_index] = arr[min_index], arr[i]
        temp= arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
# Example usage
arr = [4,5,2,3,1]
print("Original array:", arr)
selection_sort(arr)
print("Sorted array:  ", arr)

#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [8, 4, 1, 5, 9, 2]
print("Original array:", arr)
insertion_sort(arr)
print("Sorted array:", arr)

#Quick sort
def quick_sort(arr):
    if len(arr) < 1:
        return arr  
    else:
      pivot = arr[len(arr)//2] 
      print(pivot)
      left = [x for x in arr if x < pivot]  
      right = [x for x in arr if x > pivot]
      middle = [x for x in arr if x == pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = [9, 10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

# Two Pointer
def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            print(f"Pair found: ({arr[left]}, {arr[right]})")
            return True
        elif current_sum < target:
            left += 1  
        else:
            right -= 1 

    print("No pair found")
    return False
  
arr = [1, 2, 3, 4, 6, 8, 9]  
target = 10
has_pair_with_sum(arr, target)

#Stack
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)
#         print(f"Pushed: {item}")

#     def pop(self):
#         if 0!= self.is_empty():
#             item = self.stack.pop()
#             print(f"Popped: {item}")
#             return item
#         else:
#             print("Stack is empty!")
#             return None

#     def peek(self):
#         if 0!= self.is_empty():
#             return self.stack[-1]
#         else:
#             print("Stack is empty!")
#             return None

#     def is_empty(self):
#         return len(self.stack)

#     def display(self):
#         print("Stack (top to bottom):", self.stack[::-1])

# # Example usage:
# s = Stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.display()
# print("Top element is:", s.peek())
# s.pop()
# s.display()

# #Queue
# class Queue:
#     def __init__(self):
#         self.queue = []

#     # Enqueue (insert element at rear)
#     def enqueue(self, item):
#         self.queue.append(item)
#         print(f"Enqueued: {item}")

#     # Dequeue (remove element from front)
#     def dequeue(self):
#         if 0!= self.is_empty():
#             item = self.queue.pop(0)
#             print(f"Dequeued: {item}")
#             return item
#         else:
#             print("Queue is empty!")
#             return None

#     # Peek (view front element)
#     def peek(self):
#         if 0!= self.is_empty():
#             return self.queue[0]
#         else:
#             print("Queue is empty!")
#             return None

#     # Check if queue is empty
#     def is_empty(self):
#         return len(self.queue) 

#     # Display the queue
#     def display(self):
#         print("Queue (front to rear):", self.queue)


# # Example usage:
# q = Queue()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.display()
# q.dequeue()
# print("Front element is:", q.peek())
# q.display()

# #Double Queue
# from collections import deque
# class Deque:
#     def __init__(self):
#         self.deque = deque()

#     # Insert at front
#     def insert_front(self, item):
#         self.deque.appendleft(item)
#         print(f"Inserted at front: {item}")

#     # Insert at rear
#     def insert_rear(self, item):
#         self.deque.append(item)
#         print(f"Inserted at rear: {item}")

#     # Delete from front
#     def delete_front(self):
#         if not self.is_empty():
#             item = self.deque.popleft()
#             print(f"Deleted from front: {item}")
#             return item
#         else:
#             print("Deque is empty!")
#             return None

#     # Delete from rear
#     def delete_rear(self):
#         if not self.is_empty():
#             item = self.deque.pop()
#             print(f"Deleted from rear: {item}")
#             return item
#         else:
#             print("Deque is empty!")
#             return None

#     # Peek front
#     def peek_front(self):
#         if not self.is_empty():
#             return self.deque[0]
#         else:
#             print("Deque is empty!")
#             return None

#     # Peek rear
#     def peek_rear(self):
#         if not self.is_empty():
#             return self.deque[-1]
#         else:
#             print("Deque is empty!")
#             return None

#     # Check if empty
#     def is_empty(self):
#         return len(self.deque) == 0

#     # Display the deque
#     def display(self):
#         print("Deque (front to rear):", self.deque)


# # Example usage:
# dq = Deque()
# dq.insert_rear(10)
# dq.insert_rear(20)
# dq.insert_front(5)
# dq.display()

# print("Front element:", dq.peek_front())
# print("Rear element:", dq.peek_rear())

# dq.delete_front()
# dq.delete_rear()
# dq.display()

# # Node class
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.address = None

# # Linked List class
# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert at the end
#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         else:
#             last = self.head
#             while last.address != None:
#                 last = last.address
#             last.address = new_node

#     # Delete a node by value
#     def delete(self, key):
#         temp = self.head

#         # Case 1: Head node holds the key
#         if temp is not None and temp.data == key:
#             self.head = temp.address
#             temp = None
#             # return

#         # Case 2: Search for the key
#         prev = None
#         while temp is not None and temp.data != key:
#             prev = temp
#             temp = temp.address

#         # Case 3: Key not found
#         if temp is None:
#             print("Value not found in the list")
#             return

#         # Case 4: Key found and deleted
#         prev.address = temp.address
#         temp = None

#     # Display the list
#     def display(self):
#         current = self.head
#         while current != None:
#             print(current.data)
#             current = current.address
#         print("None")


# # Test the LinkedList
# llist = LinkedList()
# llist.insert(10)
# llist.insert(20)
# llist.insert(30)
# print("Linked List after insertion:")
# llist.display()  # ✅ Don't wrap in print()

# llist.delete(20)
# print("Linked List after deletion of 20:")
# llist.display()

# #Tree
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.children = []

# class Tree:
#     def __init__(self):
#         self.root = None

#     def add(self,data,parentdata = None):
#         node = TreeNode(data)

#         if not self.root:
#             self.root = node
#             return

#         ParentNode = self.findNode(parentdata,self.root)

#         if not ParentNode:
#             print("ParentNode not found")
#             return

#         ParentNode.children.append(node)


#     def findNode(self,parentdata,node):
#         if node.data == parentdata:
#             return node

#         for child in node.children:
#             nodefound = self.findNode(parentdata,child)
#             if nodefound :
#                 return nodefound

#         return None

#     def display(self,depth=0, node = None):
#         if not node:
#             node = self.root
#         print(" "*depth,node.data)

#         for child in node.children:
#             self.display(depth+1,child)

#     def remove(self, data):
#         if not self.root:
#             print("Tree is empty")
#             return

#         if self.root.data == data:
#             self.root = None
#             return

#         ParentNode = self.findParentNode(data,self.root)

#         if ParentNode != None:
#             for child in ParentNode.children:
#                 if child.data == data:
#                     ParentNode.children.remove(child)
#                     return
#         print("Node not found")

#     def findParentNode(self,data,node):
#         for child in node.children:
#             if child.data == data:
#                 return node
#             nodefound = self.findParentNode(data,child)
#             if nodefound:
#                 return nodefound

#         return None


# tree = Tree()
# tree.add(1)
# tree.add(2,1)
# tree.add(3,1)
# tree.add('a',1)
# tree.add(4,2)
# tree.add(5,2)
# tree.add(6,3)
# tree.add(7,3)
# tree.display()
# tree.remove('a')
# tree.display()

# # Binary tree
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def add(self,data):
#         if self.root is None:
#             self.root = Node(data)
#             return

#         self.recursiveAdd(data,self.root)

#     def recursiveAdd(self,data, node):
#         if  node.left is None:
#             node.left = Node(data)
#         elif node.right is None:
#             node.right = Node(data)
#         else:
#             self.recursiveAdd(data,node.left)

#     def display(self,depth=0,node=None):
#         if  node is None :
#             node = self.root

#         print(" "*depth,node.data)

#         if node.left is not None:
#             self.display(depth+1,node.left)
#         if node.right is not None:
#             self.display(depth+1,node.right)

#     def remove(self,data):
#         if  self.root is None:
#             print("Binary Tree is Empty")
#             return

#         if self.root.data == data:
#             self.root = None
#             return

#         self.recursiveRemove(data,self.root)

#     def recursiveRemove(self,data,node):
#         if node.left is not None and node.left.data == data:
#             node.left = None
#             return
#         if node.right is not None and node.right.data == data:
#             node.right = None
#             return

#         if node.left is not None:
#             self.recursiveRemove(data,node.left)
#         if node.right is not None:
#             self.recursiveRemove(data,node.right)

#     def search(self,data):
#         nodefound = self.recursiveSearch(data,self.root)
#         if nodefound is not None: 
#             print("True")
#         else: 
#             print("False")

#     def recursiveSearch(self,data,node):
#         if  node is None or node.data == data:
#             return node

#         return self.recursiveSearch(data,node.left) or self.recursiveSearch(data,node.right)

# binaryTree = BinaryTree()
# binaryTree.add(5)
# binaryTree.add(1)
# binaryTree.add(2)
# binaryTree.add(3)
# binaryTree.add(4)
# binaryTree.add(5)
# binaryTree.display()
# binaryTree.remove(4)
# binaryTree.display()
# binaryTree.search(3)

# # Binary Search Tree
# class BSTNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BinarysearchTree:
#     def __init__(self):
#         self.root = None
        
#     def add(self,data):
#         if self.root is None:
#             self.root  = BSTNode(data)
#             return
#         self.recursiveadd(self.root, data)
    
#     def recursiveadd(self, node, data):
#         if data < node.data:
#             if node.left is None:
#                 node.left = BSTNode(data)
#             else:
#                 self.recursiveadd(node.left, data)
#         elif data > node.data:
#                 if node.right is None:
#                     node.right = BSTNode(data)
#                 else:
#                     self.recursiveadd(node.right, data)
                    
#     def display(self):
#         result = []
#         # self.inordertraversel(self.root, result)
#         # self.preordertraversel(self.root, result)
#         self.postordertraversel(self.root, result)
#         print(result)

#     def inordertraversel(self, node, result):   # left ,root,right
#         if node is None:
#             return
#         else:
#             self.inordertraversel(node.left, result)
#             result.append(node.data)
#             self.inordertraversel(node.right, result)
            
#     def preordertraversel(self, node, result):  #root ,left ,right
#         if node is None:
#             return
#         else:
#             result.append(node.data)
#             self.preordertraversel(node.left, result)
#             self.preordertraversel(node.right, result)
            
#     def postordertraversel(self, node, result): #left ,right, root
#         if node is None:
#             return
#         else:
#             self.postordertraversel(node.left, result)
#             self.postordertraversel(node.right, result)
#             result.append(node.data)
            
#     def remove(self,data):
#         if  self.root is None:
#             print("Binary Tree is Empty")
#             return

#         if self.root.data == data:
#             self.root = None
#             return

#         self.recursiveRemove(data,self.root)

#     def recursiveRemove(self,data,node):
#         if node.left is not None and node.left.data == data:
#             node.left = None
#             return
#         elif node.right is not None and node.right.data == data:
#             node.right = None
#             return
#         elif data < node.data:
#             self.recursiveRemove(data,node.left)
#         elif data > node.data:
#             self.recursiveRemove(data,node.right)
            
#     def search(self,data):
#         node = self.recursiveSearch(self.root,data)
#         if node is not None: 
#             print("True")
#         else: 
#             print("False")

#     def recursiveSearch(self,node,data):
#         if  node is not None and node.data == data:
#             return node
#         elif data < node.data:
#             return self.recursiveSearch(node.left,data)
#         elif data > node.data:
#             return self.recursiveSearch(node.right,data)

    
# BST = BinarysearchTree()
# BST.add(45)
# BST.add(10)
# BST.add(50)
# BST.add(9)
# BST.add(11)
# BST.add(46)
# BST.add(51)
# BST.add(1)
# BST.display()
# BST.remove(1)
# BST.display()
# BST.search(10)
# BST.search(11)