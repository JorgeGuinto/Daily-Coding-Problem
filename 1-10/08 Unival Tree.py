"Given the root to a binary tree, count the number of unival subtrees."
"For example, the following tree has 5 unival subtrees:"
"   0"
"  / \\"
" 1   0"
"    / \\"
"   1   0"
"  / \\"
" 1   1"



class Node:
    
    def __init__(self, value, left, right):

        self.value = value
        self.left = left
        self.right = right

def univalTree(node):

    if(node.right == None and node.left == None):
        return True, 1
    
    rightUni, r = univalTree(node.right)
    leftUni, l = univalTree(node.left)
    count = l + r

    if(rightUni and leftUni and node.value == node.left.value and node.value == node.right.value):
        return True, (count + 1)
    else:
        return False, count

def countSubUnivalTrees(node):
    isUni, count = univalTree(node)
    return count


test1 = Node(0, Node(1,None,None), Node(0, Node(1, Node(1,None,None), Node(1,None,None)), Node(0, None, None)))
test2 = Node(1, Node(0,None, None), Node(1, None, None))

print(countSubUnivalTrees(test1))