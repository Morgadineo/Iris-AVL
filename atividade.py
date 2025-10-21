# avltree.py

class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def __init__(self):
        self.root = None

    # -------------------------
    # Funções auxiliares
    # -------------------------
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node): # retorna fator de balanceamento (0, 1, -1)
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y): # rotação simples à direita
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x): # rotação simples à esquerda
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # -------------------------
    # Inserção balanceada
    # -------------------------
    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value): # função recursiva
        if not node:
            return Node(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        # Atualizar altura
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Balancear
        balance = self.get_balance(node)
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # -------------------------
    # Funções de busca e info
    # -------------------------
    def height(self):
        return self.get_height(self.root)

    def size(self):
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)
        return count_nodes(self.root)

    # -------------------------
    # Encontrar o nó mais próximo
    # -------------------------
    def find_closest(self, key):
        return self._find_closest(self.root, key, None)

    def _find_closest(self, node, key, closest):
        if not node:
            return closest
        if closest is None or abs(node.key - key) < abs(closest.key - key):
            closest = node
        if key < node.key:
            return self._find_closest(node.left, key, closest)
        else:
            return self._find_closest(node.right, key, closest)
