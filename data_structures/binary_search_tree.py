class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, value):
        if(current.value < value):
            if(current.right):
                self.insert_helper(current.right, value)
            else:
                current.right = Node(value)
        else:
            if(current.left):
                self.insert_helper(current.left, value)
            else:
                current.left = Node(value)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if(current):
            if(current.value == find_val):
                return True
            elif(current.value < find_val):
                self.search_helper(current.right, find_val)
            else:
                self.search_helper(current.left, find_val)
        return False

    def tprint(self):
        tree = self.print_tree_helper(self.root, [])
        return "-".join(map(str, tree))

    def print_tree_helper(self, current, traversal):
        if(current):
            traversal.append(current.value)
            self.print_tree_helper(current.left, traversal)
            self.print_tree_helper(current.right, traversal)
        return traversal

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
# print(tree.search(4))
# print(tree.tprint())
# Should be False
print(tree.search(6))
print(tree.search(3))
