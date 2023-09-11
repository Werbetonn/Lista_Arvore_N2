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

    def encontrar_caminho(self, valor):
        def buscar_caminho_recursivo(no, valor_alvo, caminho):
            if no is None:
                return None
            caminho.append(no.valor)

            if no.valor == valor_alvo:
                return caminho

            caminho_esquerda = buscar_caminho_recursivo(no.esquerda, valor_alvo, caminho.copy())
            caminho_direita = buscar_caminho_recursivo(no.direita, valor_alvo, caminho.copy())
            return caminho_esquerda or caminho_direita

        caminho = buscar_caminho_recursivo(self.raiz, valor, [])
        return caminho

# Exemplo
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8) 
arvore.mostrar_pre_ordem()

valor_alvo = 4
caminho = arvore.encontrar_caminho(valor_alvo)
if caminho:
    print(f"\nCaminho da raiz até o nó {valor_alvo}: {caminho}")
else:
    print(f"\nNó {valor_alvo} não encontrado na árvore.")