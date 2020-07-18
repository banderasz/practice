from Node import Node

"""Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
and deserialize(s), which deserializes the string back into the tree. """


def serialize(root: Node):
    text_serialized = ""
    text_serialized += str(root.val) + "("
    if root.left:
        text_serialized += serialize(root.left)
    text_serialized += ","
    if root.right:
        text_serialized += serialize(root.right)
    text_serialized += ")"
    return text_serialized


def deserialize(s: str):
    val_index = None
    sep_index = None
    for i in range(len(s)):
        if s[i] == '(':
            val_index = i
            break
    depth = 0
    if val_index:
        for i in range(val_index+1,len(s)):
            if s[i] == '(':
                depth += 1
            elif s[i] == ')':
                depth -= 1
            if s[i] == ',' and depth == 0:
                sep_index = i
    val = s[:val_index]
    if sep_index is None:
        return Node(val)
    else:
        left = s[val_index+1:sep_index]
        right = s[sep_index+1:len(s)-1]
        if left:
            leftNode = deserialize(left)
        else:
            leftNode = None
        if right:
            rightNode = deserialize(right)
        else:
            rightNode = None
        return Node(val, leftNode, rightNode)


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
