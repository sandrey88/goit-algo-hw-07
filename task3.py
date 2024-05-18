from avl_tree import root

# Функція обчислення суми всіх значень в AVL-дереві
def find_sum(root):

    if root is None:
        return 0

    # Рекурсивне обчислення суми значень в лівому та правому піддеревах
    left_sum = find_sum(root.left)
    right_sum = find_sum(root.right)

    # Додаємо значення поточного вузла до суми піддерев
    return root.key + left_sum + right_sum

total_sum = find_sum(root)
print(f"Сума всіх значень в AVL-дереві: {total_sum}")