class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self.inserir_em_nivel_recursivo(valor, self.raiz)

    def inserir_em_nivel_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self.inserir_em_nivel_recursivo(valor, no.direita)


    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print("A árvore está vazia.")
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=" ")
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def arvore_de_busca(self):
        return self.arvore_de_busca_recursivo(self.raiz, float('-inf'), float('inf'))

    def arvore_de_busca_recursivo(self, no, min_valor, max_valor):
        if no is None:
            return True

        if no.valor <= min_valor or no.valor >= max_valor:
            return False

        return (self.arvore_de_busca_recursivo(no.esquerda, min_valor, no.valor) and
                self.arvore_de_busca_recursivo(no.direita, no.valor, max_valor))

#Exemplo
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

if arvore.arvore_de_busca():
    print("A árvore é uma árvore de busca válida.")
else:
    print("A árvore não é uma árvore de busca válida.")
