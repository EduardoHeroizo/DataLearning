import pandas as pd

df = pd.DataFrame({
    "Produto": ["Notebook","Mouse","Mesa","Cadeira","Teclado","Monitor","Cabo HDMI"],
    "Categoria": ["Eletrônico","Eletrônico","Móveis","Móveis","Eletrônico","Eletrônico","Eletrônico"],
    "Preco": [3500, 80, 700, 500, 150, 1200, 60],
    "Quantidade": [2, 10, 1, 3, 5, 2, 15],
    "Cidade": ["SP","RJ","SP","MG","RJ","SP","RJ"]
})

print(df[df["Produto"] == "Mesa"])