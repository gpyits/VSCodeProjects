# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:
# - push(x: int) -> None: Pushes element x to the top of the stack.
# - pop() -> int Removes the element on the top of the stack and returns it.
# - empty() -> bool Returns true if the stack is empty, false otherwise.
class MyStack:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self, x: int) -> None:
        self.q2.append(x)
    def pop(self) -> int:
        if self.q2: return self.q2.pop()
    def top(self) -> int:
        if self.q2: return self.q2[-1]
    def empty(self) -> bool:
        return not self.q1 and not self.q2

mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True