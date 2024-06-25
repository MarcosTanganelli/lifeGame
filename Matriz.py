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
        
    def clickButton(self, linha, coluna):
        button = self.matriz[linha][coluna]
        valor = not Cell.getLife(self.lifeMatriz[linha][coluna])
        Cell.setLife(self.lifeMatriz[linha][coluna], valor)
        if valor:
            button.configure(style='blue.TButton')
        else:
            button.configure(style='gray.TButton')
            
            
    def criarMatriz(self, janela, linhas, colunas):
        matriz = []
        style = ttk.Style()
        style.configure("gray.TButton", background="light gray")
        style.configure("blue.TButton", background="light blue")
        
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                button = ttk.Button(janela, text=f'({i},{j})',  style='gray.TButton', command=lambda linha=i, coluna=j: self.clickButton(linha, coluna))
                button.grid(row=i, column=j)
                linha.append(button)
            matriz.append(linha)
        return matriz

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Life Game")
    Matriz(janela)
    janela.mainloop()
