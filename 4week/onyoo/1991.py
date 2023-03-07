from sys import stdin

n = int(stdin.readline())
tree = {}


for _ in range(n):
    node = list(stdin.readline().split())
    tree[node[0]] = node[1:]


def preorder(node):
    if not node or node == '.':
        return
    print(node,end="")
    branch = tree[node]
    preorder(branch[0])
    preorder(branch[1])

def inorder(node):
    if not node or node == '.':
        return
    branch = tree[node]
    inorder(branch[0])
    print(node, end="")
    inorder(branch[1])

def postorder(node):
    if not node or node == '.':
        return
    branch = tree[node]
    postorder(branch[0])
    postorder(branch[1])
    print(node, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')
