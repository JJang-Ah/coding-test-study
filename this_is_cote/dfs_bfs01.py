

#스택
stack = []
stack.append(1)
stack.append(4)
stack.append(2)
stack.pop()
stack.append(9)
stack.append(8)

print("stack: " ,stack)
print("stack[::-1]: " ,stack[::-1])



from collections import *
q = deque()

q.append(1)
q.append(4)
q.append(3)
q.pop()
q.append(8)

print(q)
q.reverse()
print(q)