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

class Arvore:
    def __init__(self):
        self.arvore_binaria = ArvoreBinaria()

    def inserir_valor(self, valor):
        self.arvore_binaria.inserir_em_nivel(valor)

#Exemplo
minha_arvore = Arvore()
minha_arvore.inserir_valor(5)
minha_arvore.inserir_valor(3)
minha_arvore.inserir_valor(7)
minha_arvore.inserir_valor(2)
minha_arvore.inserir_valor(4)
minha_arvore.inserir_valor(6)
minha_arvore.inserir_valor(8)
minha_arvore.arvore_binaria.mostrar_pre_ordem()