from .node import Node


class AvlTree:
    def __init__(self, data) -> None:
        self.root = data

    def push(self, data):
        """Recebe um dado como argumento e insere um novo nó
        na árvore já a balanceando com o dado armazenado."""

        if self.root is None:
            self.root = Node(data)
            return

    def pop(self, data):
        """Recebe um dado como argumento e remove um novo nó
        na árvore já a balanceando que contenha este dado."""
        raise NotImplemented

    def find(self, data):
        """Recebe um dado como argumento e busca um novo nó
        na árvore retornando True se o dado existir e False
        caso não exista."""
        raise NotImplemented

    def __is_balanced(self):
        """Checa se a árvore está balanceada ou não,
        retorna True, caso esteja e False caso não esteja."""
        raise NotImplemented
