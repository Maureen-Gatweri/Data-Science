
from collections import deque
q = deque ()
q.append("Nairobi")
q.append("Meru")
q.append("Mombasa")
q.append("Lamu")
q.append("Nakuru")
q.append("Baringo")
q.append("Machakos")
q.append("Kakamega")
q.append("Chebarbar")
print(q)
print(type(q))
print(q)
print(q.pop())
print(q)

#removing elements from a queue
print("\nElements dequeued from queue")
print(q.pop())
print(q.pop())

#Removing elements from the first one
print(q.popleft())
#queue after removing two elements
print(q)

#Accesing elements using index
print(q[2])
print(q[0])

