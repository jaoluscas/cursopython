import importlib

import aula98_m

print(aula98_m.variavel)

# TESTE PARA PROVAR QUE O PYTHON NÃO IMPORTA UM MODULO "SINGLETON" VARIAS VEZES. ha não ser que use a biblioteca importlib com a função reload.

for i in range(10):
    importlib.reload(aula98_m)
    import aula98_m

print("fim")