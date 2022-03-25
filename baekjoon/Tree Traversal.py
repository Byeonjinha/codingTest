class Node:
    def __init__(self,data, left_node, right_node):
        n=0
        self.data=data
        self.left_node = left_node
        self.right_node = right_node
        n=n+1



#전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node !=None:
        pre_order(tree[node.left_node])
    if node.right_node !=None:
        pre_order(tree[node.right_node])
#중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data,end=" ")
    if node.right_node != None:
        in_order(tree[node.right_node])

#후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")


def solution(info, edges):
    answer = 0
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges=[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)

tree = {}
for i in range(len(info)):
    data = info[i]
    left_node, right_node = input().split()
    if left_node =="None":
        left_node = None
    if right_node =="None":
        right_node = None
    tree[data] =Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

'''
예제
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
'''

'''
예제2
9
50 30 98
30 24 45
24 5 28
5 None None
28 None None
45 None None
98 52 None
52 None 60
60 None None
'''