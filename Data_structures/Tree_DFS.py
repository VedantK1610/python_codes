'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def dfs_inorder(node):
    if not node:
        return
    dfs_inorder(node.left)
    print(node.data,end=' ')
    dfs_inorder(node.right)

def dfs_preorder(node):
    if not node:
        return
    print(node.data,end=' ')
    dfs_preorder(node.left)
    dfs_preorder(node.right)


def dfs_postorder(node):
    if not node:
        return
    dfs_postorder(node.left)
    dfs_postorder(node.right)
    print(node.data,end=' ')


def get_height(root):
    # number of edges from root to deepest node
    # get max depth of left sub tree and right sub tree
    # then calculate 1+max(left,right)
    if root is None:
        return -1
    left = get_height(root.left)
    right = get_height(root.right)

    return 1 + max(left, right)


t=TreeNode(1)
t.left=TreeNode(3)
t.left.left=TreeNode(2)
t.left.right=TreeNode(4)
t.right=TreeNode(5)

# dfs_inorder(t)
print(get_height(t))

'''
        1 
    3       5
 2     4
'''
