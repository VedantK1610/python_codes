'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#each time we print one element of level i-1 , we pop that printed element and add all elements of level i in queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while (len(queue) > 0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

bfs(root)

'''
        1 
    2       3
4     5
'''