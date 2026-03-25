
# ________________________________________________________

1. Array?

 Array is a data structure that stores elements in continuous memory locations and allows fast access using index.
 Types of Arrays?
     1. Static Array --> Each element is stored next to each other.

     2. Dynamic Array -->random places la store aagum.

     Static → fixed size
    Dynamic → resizable

# ________________________________________________________

2. why mostly list use?

    Because Python is designed for:
        Simplicity
        Flexibility
        Developer productivity
    And list is more powerful & flexible than array.



| Feature       | Continuous Memory | Dynamic / Non-Continuous |
| ------------- | ----------------- | ------------------------ |
| Storage       | Side by side      | Random places            |
| Example       | Array             | Linked List              |
| Access speed  | O(1)              | O(n)                     |
| Insert/Delete | O(n)              | O(1)                     |
| Memory need   | Continuous block  | Any free space           |


# ________________________________________________________


## 1️⃣ O(1) – Constant Time
## 2️⃣ O(n) – Linear Time
## 3️⃣ O(n²) – Quadratic
## 4️⃣ O(log n) – Logarithmic
## 5️⃣ O(n log n)


# Big-O Notation 
## What is Big-O?
# Why Big-O is Used?
    we measure:**How algorithm grows when input grows*

# Growth Comparison
   If n = 1000:
| Complexity | Steps     |
| ---------- | --------- |
| O(1)       | 1         |
| O(log n)   | ~10       |
| O(n)       | 1000      |
| O(n log n) | ~10,000   |
| O(n²)      | 1,000,000 |


# ________________________________________________________
🔹 HashMap / Dictionary
# ________________________________________________________


      Hashing technique--->Key → converted to hash value → stored in memory location.
      O(1) Average Access Time
      Hash Value = Key-a computer fast-a locate panna or store panna use panra number
                   Key = "name"
                   Computer doesn’t directly search "name" in memory (slow)
                   Instead, "name" convert pannuvom to a unique number → called hash value


#     Important Points (3-Year Dev Level)

      Keys are immutable → because only immutable objects can have stable hash values
                            e.g., string, int, tuple

      Mutable objects like list → cannot be key
      Collision → different keys can have same hash value
      Python handles it internally
      Hash value is internal → you rarely need to use directly
      But knowing the concept helps optimize algorithms


#    “What is hash value?”
        
        “Hash value is a number generated from a key using a hash function. Python uses it internally to store and access the value fast in a dictionary, giving O(1) average lookup time


       | Feature           | Why Important          |
       | ----------------- | ---------------------- |
       | Key-value storage | Mapping relationships  |
       | Fast lookup       | Optimizing brute force |
       | O(1) average time | Scalability            |
       | Unique keys       | Avoid duplication      |
       | Hashing           | Internal mechanism     |


#  what is dictionary?
    
    Keys must be immutable (string, int, tuple).
    Values can be mutable or immutable.
    Python dict internally uses hash table.
    Average access → O(1).
    Very useful for mapping, frequency counting, caching, grouping.



# Why is it faster than list search?

     List → sequential scan → slow for large data
     Dict → scalable, optimized for fast lookup




# What is Linked List?

   Linked list is a linear data structure where elements are stored as nodes, and each node is connected to the next node using a pointer/reference.


   Array / List la → element = data
   Linked List la → element = node (data + pointer)



# “How is a linked list implemented in Python?”
   
     A linked list is implemented using a class-based node structure. Each node contains data and a reference to the next node, and nodes are connected using the next pointer starting from the head.


     Using Python Built-in Libraries
     collections.deque

     from collections import deque
     d = deque([10, 20, 30])
     d.appendleft(5)

     This is not exactly a linked list
     It is a double-ended queue
     Internally optimized



# When will you use Linked List over Array?
      When frequent insert/delete operations required
      When size unpredictable
      When implementing stack, queue, LRU cache

# When Array is better?
     
     When frequent random access required
     When memory optimization important
     When fixed size known

# When Python List is better?
     General purpose
     Easy coding
     Most application-level development

# ________________________________________________________

| Feature         | Python List | Array      | Linked List    |
| --------------- | ----------- | ---------- | -------------- |
| Memory          | Continuous  | Continuous | Non-contiguous |
| Size            | Dynamic     | Fixed      | Dynamic        |
| Data Type       | Mixed       | Same type  | Same or mixed  |
| Access by Index | O(1)        | O(1)       | O(n)           |
| Insert Middle   | O(n)        | O(n)       | O(1)*          |
| Delete Middle   | O(n)        | O(n)       | O(1)*          |
| Extra Memory    | No          | No         | Yes (pointer)  |


# ________________________________________________________


# What is Binary Tree?
     A binary tree is a hierarchical data structure in which each node has at most two children, called the left child and right child.


# One line memory trick

     Type	                  Order	        Easy memory
     Preorder	              Root first	Parent first
     Inorder	                 Root middle	Parent middle
     Postorder	              Root last	     Parent last


# ________________________________________________________
