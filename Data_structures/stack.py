from collections import deque

stack=deque()

stack.append(1)
stack.append(2)
stack.append(4)
stack.append(3)

print(stack)

stack.pop()
stack.popleft()
print(stack)

stack.appendleft(0)
print(stack)