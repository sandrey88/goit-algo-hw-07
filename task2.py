from avl_tree import root

# Функція для пошуку найменшого значення в AVL-дереві
def find_min(root):
    if root is None:
        return None

    # Ітеративно переходимо вліво, оскільки в AVL-дереві найменше значення завжди знаходиться в найлівішому вузлі
    while root.left is not None:
        root = root.left

    return root.key  # Повертаємо значення найлівішого вузла

min_value = find_min(root)
print(f"Найменше значення в AVL-дереві: {min_value}")