"Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree."
"For example, given the following Node class"
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"The following test should pass:"
"node = Node('root', Node('left', Node('left.left')), Node('right'))"
"assert deserialize(serialize(node)).left.left.val == 'left.left'"

def serialize(node):
    val = node.val

    if node.left != None:
        left = serialize(node.left)
    else:
        left = None

    if node.right != None:
        right = serialize(node.right)
    else:
        right = None
    
    serialized = [val, left, right]
    return serialized

def deserialize(serializedNode):
    val = serializedNode[0]
    if serializedNode[1]:
        left = deserialize(serializedNode[1])
    else:
        left = None
    if serializedNode[2]:
        right = deserialize(serializedNode[2])
    else:
        right = None
    return Node(val, left, right)


node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))

deserialize(serialize(node)).left.left.val == 'left.left'