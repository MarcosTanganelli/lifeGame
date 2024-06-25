import tkinter as tk
from tkinter import ttk

from Cell import Cell

class Matriz:
    def __init__(self, janela, linha = 3, coluna= 3):
        self.linha = linha
        self.coluna = coluna
        self.matriz = self.criarMatriz(janela, 3, 3)
        self.lifeMatriz = []
        for x in range(self.linha):
            linha = []
            for y in range(self.coluna):
                linha.append(Cell(0)) 
            self.lifeMatriz.append(linha)
        # print(self.lifeMatriz)
        
    def clique_botao(self, i, j):
        print(f'Clicou em ({i},{j})')
            
    def criarMatriz(self, janela, linhas, colunas):
        matriz = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                button = ttk.Button(janela, text=f'({i},{j})', command=lambda x=i, y=j: self.clique_botao(x, y))
                button.grid(row=i, column=j)
                linha.append(button)
            matriz.append(linha)
        return matriz

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Matriz usando ttk")
    Matriz(janela)
    janela.mainloop()
