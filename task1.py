from avl_tree import root

# Функція для пошуку найбільшого значення в AVL-дереві
def find_max(root):
    if root is None:
        return None

    # Ітеративно переходимо вправо, оскільки в AVL-дереві найбільше значення завжди знаходиться в найправішому вузлі
    while root.right is not None:
        root = root.right

    return root.key  # Повертаємо значення найправішого вузла

max_value = find_max(root)
print(f"Найбільше значення в AVL-дереві: {max_value}")