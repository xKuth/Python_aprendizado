
class BSTNode(object):
    def __init__(self, key, value=None, left=None, right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right
        root = BSTNode(8)
        root.left = BSTNode(3)
        root.right = BSTNode(10)
        root.right = BSTNode(14)
        root.left.left = BSTNode(1)
        root.left.right = BSTNode(6)
        root.left.right.left = BSTNode(4)
        root.left.right.right = BSTNode(7)
        found = root.get(4)
        if found:
            print(found)

    def get(self, key):
        if key < self.key:
            return self.left.get(key) if self.left else None
        elif key > self.key:
            return self.right.get(key) if self.right else None
        else:
            return self

