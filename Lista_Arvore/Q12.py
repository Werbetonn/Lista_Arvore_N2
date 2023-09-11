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

    def encontrar_sucessor(self, no):
        atual = no.direita
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover_no(self, valor):
        self.raiz = self.remover_no_recursivo(self.raiz, valor)
        if self.raiz is not None:
            print(f"\nO nó com valor {valor} foi removido.")
        else:
            print(f"\nO nó com valor {valor} não existe na árvore.")

    def remover_no_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self.remover_no_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover_no_recursivo(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda

            sucessor = self.encontrar_sucessor(no)
            no.valor = sucessor.valor
            no.direita = self.remover_no_recursivo(no.direita, sucessor.valor)
        return no

#Exemplo
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
arvore.remover_no(5)

print("\nA árvore após remover o nó:")
arvore.mostrar_pre_ordem()
