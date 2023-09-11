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

    def obter_filhos(self, valor_pai):
        def buscar_no_e_retornar_filhos(no, valor):
            if no is None:
                return []

            if no.valor == valor:
                filhos = []
                if no.esquerda is not None:
                    filhos.append(no.esquerda.valor)
                if no.direita is not None:
                    filhos.append(no.direita.valor)
                return filhos

            return (buscar_no_e_retornar_filhos(no.esquerda, valor) +
                    buscar_no_e_retornar_filhos(no.direita, valor))

        return buscar_no_e_retornar_filhos(self.raiz, valor_pai)

#Exemplo
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)

arvore.mostrar_pre_ordem()
print()

no_pai = 3
filhos = arvore.obter_filhos(no_pai)
print(f"Filhos do nó {no_pai}: {filhos}")