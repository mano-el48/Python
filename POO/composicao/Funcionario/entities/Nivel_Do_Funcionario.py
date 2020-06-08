from enum import Enum

class Nivel_Do_Funcionario(Enum):
    JUNIOR = 'JUNIOR'
    MID_LEVEL = 'MID_LEVEL'
    SENIOR = 'SENIOR'

nivel = 'MID_LEVEL'
print(Nivel_Do_Funcionario[nivel].value)


