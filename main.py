url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

# Sanitização(validação) da URL
url = url.replace(" ", "").strip()

if url == "":
    raise ValueError('A URL está vazia.')

# Separa base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)

'''
Para fazer com que sua classe tenha alguns comportamentos específicos, você pode implementar o que chamamos de métodos especiais, como __len__, __str__ e __eq__. Cada um desses métodos é chamado indiretamente pelo próprio interpretador Python quando executamos algumas instruções específicas.

Por exemplo:

objeto = MinhaClasse()

print(objeto)  # => invoca o método objeto.__str__()
len(objeto)  # => invoca o método objeto.__len__()

outro_objeto = MinhaClasse()
objeto == outro_objeto  # => invoca o método objeto.__eq__(outro_objeto)
'''