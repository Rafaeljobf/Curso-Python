# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'teste_shutil')
NOVA_PASTA = os.path.join(DESKTOP, 'teste2_shutil')

# shutil.move(NOVA_PASTA, NOVA_PASTA + '_OPA')
# shutil.rmtree(NOVA_PASTA + '_OPA')
# shutil.rmtree(PASTA_ORIGINAL)
# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)