class Node:
    def __init__(self, val, key=None, left=None, right=None):
        self.value = val
        self.key = key
        self.left = left
        self.right = right


class Tree():
    def __init__(self):
        self.rootTree = None

    def insert(self, root, data, key=None):
        if root is None:
            return Node(data, key)
        else:
            if key <= root.key:
                cur = self.insert(root.left, data, key)
                root.left = cur
            else:
                cur = self.insert(root.right, data, key)
                root.right = cur
        return root

    def getHeight(self, root):
        """the maximum number of edges = level of tree - 1"""
        if root is None:
            return -1
        l = self.getHeight(root.left)
        r = self.getHeight(root.right)
        if l > r:
            return l+1
        else:
            return r+1

# traversal:


def inOrd(root) -> str:
    '''
    inorder traversal
    '''
    string = ''
    if root:
        string += inOrd(root.left)
        string += f' {root.value}'
        string += inOrd(root.right)
    return string


def preOrd(root) -> str:
    '''
    pre order traversal
    '''
    string = ''
    if root:
        string += f' {root.value}'
        string += preOrd(root.left)
        string += preOrd(root.right)
    return string


def PostOrd(root):
    '''
    post order traversal
    '''
    string = ''
    if root:
        string += PostOrd(root.left)
        string += PostOrd(root.right)
        string += f' {root.value}'
    return string


def levelData(root, level):
    string = ''
    if root:
        if level == 1:
            string += (str(root.value) + ' ')
        elif level > 1:
            string += levelData(root.left, level-1)
            string += levelData(root.right, level-1)
    return string


def levelOrd(root):
    # Write your code here
    t = Tree()
    h = t.getHeight(root)
    output = ''
    for i in range(1, h+2):
        output += levelData(root, i)
    return output


def serialize(root) -> str:
    '''
    generate string form binary tree
    '''
    string = ''
    string = inOrd(root)
    return string


def deserialize(str_: str) -> Node:
    """
    generate tree for string
    """
    global node
    from_root = list(preOrd(node).split(' '))
    list_str = str_.split(' ')
    new_tree = Tree()
    root = None
    for e in from_root[1::]:
        index = list_str.index(e)
        # insert something Here
        root = new_tree.insert(root, e, index)
    return root


if __name__ == "__main__":
    # construct the tree
    node = Node(val='root', left=Node(
        val='left', left=Node(val='left.left')), right=Node(val='right'))
    print(serialize(node))
    assert deserialize(serialize(node)).left.left.value == 'left.left'
