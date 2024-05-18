import matplotlib.pyplot as plt

class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

# Функція для візуалізації AVL-дерева
def plot_avl_tree(node, pos=None, level=0, xcenter=0, dx=1.0):
    if node is None:
        return

    if pos is None:
        pos = {}

    pos[node.key] = (xcenter, -level)

    plot_avl_tree(node.left, pos, level + 1, xcenter - dx, dx / 2)
    plot_avl_tree(node.right, pos, level + 1, xcenter + dx, dx / 2)

    return pos

def draw_avl_tree(root):
    pos = plot_avl_tree(root)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title('AVL Tree')
    ax.set_axis_off()

    for key, (x, y) in pos.items():
        ax.text(x, y, str(key), ha='center', va='center', bbox=dict(facecolor='skyblue', boxstyle='round,pad=0.5'))
        node = find_node(root, key)
        if node.left:
            lx, ly = pos[node.left.key]
            ax.plot([x, lx], [y, ly], 'k-')
        if node.right:
            rx, ry = pos[node.right.key]
            ax.plot([x, rx], [y, ry], 'k-')
    plt.show()

def find_node(root, key):
    if root is None:
        return None
    if root.key == key:
        return root
    if key < root.key:
        return find_node(root.left, key)
    else:
        return find_node(root.right, key)

# Створення AVL-дерева та вставка 7 вузлів
avl_tree = AVLTree()
root = None

nodes = [10, 20, 30, 40, 50, 25, 5]

for node in nodes:
    root = avl_tree.insert(root, node)

# Візуалізація дерева
draw_avl_tree(root)
