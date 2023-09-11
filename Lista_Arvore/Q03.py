class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def verificar_valor(self, valor):
        return self._verificar_valor_recursivo(self.raiz, valor)

    def _verificar_valor_recursivo(self, no, valor):
        if no is None:
            return "O valor não está presente na árvore."
        if no.valor == valor:
            return "O valor está presente na árvore."
        if valor < no.valor:
            return self._verificar_valor_recursivo(no.esquerda, valor)
        return self._verificar_valor_recursivo(no.direita, valor)

#Exemplo
arvore = ArvoreBinaria()
arvore.inserir(5)
arvore.inserir(3)
arvore.inserir(7)
arvore.inserir(2)
arvore.inserir(4)
arvore.inserir(6)
arvore.inserir(8)

print(arvore.verificar_valor(5))
print(arvore.verificar_valor(8))
print(arvore.verificar_valor(10))
