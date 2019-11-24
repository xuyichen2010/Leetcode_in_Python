# https://www.geeksforgeeks.org/using-list-stack-queues-python/
# STACK
# Python code to demonstrate Implementing
# stack using list
stack = ["Amar", "Akbar", "Anthony"]
stack.append("Ram")
stack.append("Iqbal")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# QUEUE
# https://www.geeksforgeeks.org/deque-in-python/
# Python code to demonstrate Implementing
# Queue using deque and list
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])

queue.appendleft("Akbar")

queue.append("Birbal")

print(queue.popleft())
print(queue.pop())
