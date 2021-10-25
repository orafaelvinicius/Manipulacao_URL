endereco = "Rua das Flores, Amarante, São Gonaçalo do Amarante, RN, 59296-000"

import re  # Regular Expression -- RegEx

# 5 dígitos + híven (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
