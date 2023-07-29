from enum import Enum


class ResidenceType(Enum):
    APARTAMENTO = 0
    MORADIA = 1


class Condition(Enum):
    RUINA = "Ruína"
    NOVO = "Novo"
    RENOVADO = "Renovado"
    USADO = "Usado"
    EM_CONSTRUCAO = "Em construção"
    PARA_RECUPERAR = "Para recuperar"
