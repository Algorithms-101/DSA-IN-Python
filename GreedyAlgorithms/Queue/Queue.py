# Implementing a Queue

# Import doubly ended queue module.
from collections import deque

# Initialize queue.
q = deque()

# Include values in Queue
q.append('first value')
q.append('second value')
q.append('third value')

print("first queue")

print(q)

# Remove values in a queue
print("\nValues removed from the queue")

print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nCurrent Values after removal")
print(q)
