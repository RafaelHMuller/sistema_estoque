#!/usr/bin/env python
# coding: utf-8

# # Desafio Python-SQL e Tkinter
# 
# A partir da criação de uma janela (recriar a janela Tkinter por meio do Sigma.com e Proxlight Designer) para controle de estoque, adicionar dentro das funções códigos (CRUD) que integrem o Python ao banco de dados SQL.

# In[1]:


from tkinter import *
import pyodbc


# - Integrar o banco de dados SQL ao Python

# In[2]:


dados_conexao = ('Driver={SQLite3 ODBC Driver}; Server=localhost; Database=Estoque.db')
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


# - Definir as funções dos botões da janela Tkinter <br>
# 
# Colar aqui o código .py da janela Tkinter criado pelo Proxlight Designer

# In[3]:


############### definição dos botões ###############

def adicionar():
    cursor.execute(f'''
    INSERT INTO Estoque (Produto, Quantidade, DataValidade, Lote)
    VALUES ("{nome_insumo.get()}", "{qtde_insumo.get()}", "{data_insumo.get()}", "{lote_insumo.get()}")
    ''')
    cursor.commit()
    
    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"Item {nome_insumo.get()} adicionado ao estoque!")
    

def deletar():
    if len(nome_insumo.get()) < 1:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Nome do item inválido!")
        return
    else:
        cursor.execute(f'DELETE FROM Estoque WHERE Produto = "{nome_insumo.get()}"')
        cursor.commit()
        
    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"Item {nome_insumo.get()} deletado!")
    

def consumir():
    if len(nome_insumo.get()) < 1 or len(lote_insumo.get()) < 1 or len(qtde_insumo.get()) < 1:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Nome do item, lote ou quantidade do item inválido!")
        return
    else:
        cursor.execute(f'''
        UPDATE Estoque SET Quantidade=Quantidade-"{qtde_insumo.get()}" 
        WHERE Produto="{nome_insumo.get()}" AND Lote="{lote_insumo.get()}"
        ''')
        cursor.commit()
    
    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"Item {nome_insumo.get()} alterado em {qtde_insumo.get()} unidades!")
    

def procurar():
    if len(nome_insumo.get()) < 1:
        caixa_texto.delete("1.0", END)
        caixa_texto.insert("1.0", "Nome do item inválido!")
        return
    else:
        cursor.execute(f'SELECT * FROM Estoque WHERE Produto="{nome_insumo.get()}"')
        valores = cursor.fetchall() 
        
        for tupla in valores:
            id_produto, produto, quantidade, validade, lote = tupla
            texto = f'''
Produto: {produto}
Quantidade: {quantidade:.0f}
Validade: {validade}
Lote: {lote}
'''
    
    caixa_texto.delete("1.0", END)
    caixa_texto.insert("1.0", f"{texto}")


############### janela tkinter ###############

window = Tk()

window.geometry("769x690")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 690,
    width = 769,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"janela_revisão/background.png")
background = canvas.create_image(
    384.5, 345.0,
    image=background_img)

######## BOTÕES

img0 = PhotoImage(file = f"janela_revisão/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = procurar,
    relief = "flat")

b0.place(
    x = 544, y = 196,
    width = 178,
    height = 54)

img1 = PhotoImage(file = f"janela_revisão/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = deletar,
    relief = "flat")

b1.place(
    x = 544, y = 107,
    width = 178,
    height = 54)

img2 = PhotoImage(file = f"janela_revisão/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = adicionar,
    relief = "flat")

b2.place(
    x = 329, y = 107,
    width = 178,
    height = 54)

img3 = PhotoImage(file = f"janela_revisão/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = consumir,
    relief = "flat")

b3.place(
    x = 329, y = 196,
    width = 178,
    height = 54)

######## ENTRIES (INPUTS)

entry0_img = PhotoImage(file = f"janela_revisão/img_textBox0.png")
entry0_bg = canvas.create_image(
    477.0, 464.0,
    image = entry0_img)

qtde_insumo = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

qtde_insumo.place(
    x = 366, y = 443,
    width = 222,
    height = 40)

entry1_img = PhotoImage(file = f"janela_revisão/img_textBox1.png")
entry1_bg = canvas.create_image(
    477.0, 414.0,
    image = entry1_img)

lote_insumo = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

lote_insumo.place(
    x = 366, y = 393,
    width = 222,
    height = 40)

entry2_img = PhotoImage(file = f"janela_revisão/img_textBox2.png")
entry2_bg = canvas.create_image(
    477.0, 364.0,
    image = entry2_img)

data_insumo = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

data_insumo.place(
    x = 366, y = 343,
    width = 222,
    height = 40)

entry3_img = PhotoImage(file = f"janela_revisão/img_textBox3.png")
entry3_bg = canvas.create_image(
    477.0, 314.0,
    image = entry3_img)

nome_insumo = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

nome_insumo.place(
    x = 366, y = 293,
    width = 222,
    height = 40)

######## CX DE TEXTO

entry4_img = PhotoImage(file = f"janela_revisão/img_textBox4.png")
entry4_bg = canvas.create_image(
    484.0, 599.0,
    image = entry4_img)

caixa_texto = Text(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

caixa_texto.place(
    x = 267, y = 549,
    width = 434,
    height = 98)

window.resizable(False, False)
window.mainloop()


# In[4]:


cursor.close()
conexao.close()

