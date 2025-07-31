import os

pasta = "/home/lucas-finoti/ProjetosPessoais/Pesquisa/dataset/train"

os.chdir(pasta)

imagens = [f for f in os.listdir() if f.lower().endswith('.png')]

imagens.sort()

for i, nome_original in enumerate(imagens, start=1):
    novo_nome = f"imagem_{i}.png"
    os.rename(nome_original, novo_nome)
    print(f"Renomeado: {nome_original} → {novo_nome}")

print("Renomeação concluída.")
