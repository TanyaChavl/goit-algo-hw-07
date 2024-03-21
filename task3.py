class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Використання
root = None
values = [5, 3, 2, 4, 7, 6, 8]  # Значення для вставки в дерево
for val in values:
    root = insert(root, val)

total_sum = sum_of_values(root)
print("Сума всіх значень у дереві:", total_sum)
