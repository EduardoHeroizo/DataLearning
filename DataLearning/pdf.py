import fitz  

doc = fitz.open("cartilha-redac-a-o-a-mil-lucas-felpi.pdf")

start_page_humana = 5
start_idx = start_page_humana - 1
texto = []

for i in range(start_idx, len(doc)):
    texto_pagina = doc[i].get_text("text").strip()
    
    if texto_pagina:
        texto.append(texto_pagina)

saida = "".join(texto)

with open("redacoes_extraidas.txt", "w", encoding="utf-8") as f:
    f.write(saida)

with open("ac587a5a-4000-421e-9ab4-78c861417568.txt", "r", encoding="utf-8") as f:
    texto = f.read()

redacoes = []
atual = ""

for linha in texto.splitlines():

    if "Foto:" in linha and atual != "":
        redacoes.append(atual)
        atual = ""

    atual += linha + "\n"

if atual != "":
    redacoes.append(atual)

print("Quantidade de redações:", len(redacoes))