sobrenome_autor = input('Digite o sobrenome do autor (em caixa alta): ')
nome_autor = input('Digite o primeiro nome do autor: ')
nome_site = input('Digite o nome do site (em caixa alta): ')
data = input('Digite o ano em que foi publicado: ') 
titulo_site = input('Digite o titulo do site: ')
url = input('Cole o link do site aqui: ')
data_acesso = input('Digite a data de acesso (Ex.: 22 fev 2006): ')

# Pede ao usuário todas as informações do site
site_negrito = (f"\033[1m{nome_site}\033[0m")

print(f'{sobrenome_autor}, {nome_autor}. {site_negrito}, {data}. {titulo_site}. Disponível em: {url}. Acesso em: {data_acesso}.')