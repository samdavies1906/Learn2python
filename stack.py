# Implementing a stack in python

stack = []

def push(x):
    stack.append(x)


def isEmpty():
    if len(stack) == 0:
        return true


def pop():
    stack.pop()


def top():
    if isEmpty:
        topElementIndex = len(stack)-1
        return stack[topElementIndex]

push(1)
print("push: " + str(stack))
push(2)
print("push: " + str(stack))
push(3)
print("push: " + str(stack))
pop()
print("pop: " + str(stack))
print("top: " + str(top()))
