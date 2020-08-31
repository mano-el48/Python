import pacote.sub.arquivo
from types import tipos_basicos, variaveis
from types import basic_types
import types.list
import types.tuple
import types.set
import operators.aritmeticos_atribuicao
import operators.unarios_ternarios
import operators.relacionais_logicos
import operators.membro_identidade
from functions.basico import sum
print(sum(10, 20))
print(sum(20, 20))
from functions.args import sum
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
from functions.args import result
print(result(nome = 'Sharon', nota = 6))
print(result(nome = 'Sharon', nota = 4))
from functions.funcional import sum
print(sum(10, 20))
from functions.funcional import result
print(result(sum, 10, 20))