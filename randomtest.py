class Node:
    def __init__(self):
        self.var = 'Hello'

class A:
    def __init__(self, node):
        self.current = node
    def test_a(self):
        print('This is A')
    
node = Node()
# print(node.var)
a = A(node)
b = a
b.current.var = 'Hi'
print(a)
print(b)
# print(b.current.var)
print(node.var)
