import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, data, left_node, right_node):
        self.data=data
        self.left_node= left_node
        self.right_node = right_node

#전위순회
def pre_order(node):
    print(node.data, end='')
    if node.left_node != ".":
        pre_order(tree[node.left_node])
    if node.right_node != ".":
        pre_order(tree[node.right_node])

#중위순회

def in_order(node):
    if node.left_node != ".":
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != ".":
        in_order(tree[node.right_node])
#후위순회

def post_order(node):
    if node.left_node != ".":
        post_order(tree[node.left_node])
    if node.right_node != ".":
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())
tree ={}

for i  in range(n):
    data, left_node, right_node = input().split()
    if left_node ==  ".":
        left_node = "."
    if right_node == ".":
        right_node = "."
    tree[data] = Node(data, left_node, right_node)


pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""