class TreeNode:
    """A node in the binary search tree."""
    def __init__(self, key: int):
        """
        Initializes the node with a key.

        Args:
            key: The key of the node.
        """
        self.left: 'TreeNode' | None = None
        self.right: 'TreeNode' | None = None
        self.val: int = key

class BinarySearchTree:
    """A binary search tree implementation."""
    def __init__(self):
        """Initializes the binary search tree."""
        self.root: 'TreeNode' | None = None

    def insert(self, key: int) -> None:
        """
        Inserts a new key into the tree.

        Args:
            key: The key to insert.
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node: TreeNode, key: int) -> None:
        """
        Helper function to insert recursively.

        Args:
            node: The current node to insert the key.
            key: The key to insert
        """
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

def find_max(node: TreeNode) -> int:
    """Finds the maximum value in the BST."""
    current = node
    while current.right is not None:
        current = current.right
    return current.val

def find_min(node: TreeNode) -> int:
    """Finds the minimum value in the BST."""
    current = node
    while current.left is not None:
        current = current.left
    return current.val

def find_sum(node: TreeNode | None) -> int:
    """Calculates the sum of all values in the BST."""
    if node is None:
        return 0
    else:
        return node.val + find_sum(node.left) + find_sum(node.right)

# Example of using the above implementation:
bst = BinarySearchTree()
values = [20, 10, 30, 5, 15, 25, 35]
for val in values:
    bst.insert(val)

print("Максимальне значення:", find_max(bst.root))
print("Мінімальне значення:", find_min(bst.root))
print("Сума всіх значень:", find_sum(bst.root))
