import os
import subprocess

# Função para criar um arquivo e dar commit no GitHub
def cria_arquivo_e_commit(numero):
    nome_arquivo = f"arquivo_{numero:02d}.txt"
    
    # Cria o arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"Este é o arquivo número {numero}\n")
    
    # Adiciona o arquivo ao índice do git
    subprocess.run(["git", "add", nome_arquivo])
    
    # Faz o commit com a mensagem especificada
    mensagem_commit = f"{numero:02d}"
    subprocess.run(["git", "commit", "-m", mensagem_commit])

# Função principal que executa o processo para o número especificado
def executar_processos(numero_final):
    for i in range(1, numero_final + 1):
        cria_arquivo_e_commit(i)
    
    # Apaga todos os arquivos criados
    for i in range(1, numero_final + 1):
        nome_arquivo = f"arquivo_{i:02d}.txt"
        os.remove(nome_arquivo)

# Defina o número final (por exemplo, 53)
numero_final = 53
executar_processos(numero_final)
