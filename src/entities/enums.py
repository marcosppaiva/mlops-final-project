from enum import Enum


class ResidenceType(Enum):
    APARTAMENTO = 'apartamento'
    MORADIA = 'moradia'


class Condition(Enum):
    RUINA = 'Ruína'
    NOVO = 'Novo'
    RENOVADO = 'Renovado'
    USADO = 'Usado'
    EM_CONSTRUCAO = 'Em construção'
    PARA_RECUPERAR = 'Para recuperar'


class EnergyCertify(Enum):
    E = 'E'
    D = 'D'
    F = 'F'
    C = 'C'
    ISENTO_EM_TRAMITE = 'Isento / Em Trâmite'
    A = 'A'
    A_PLUS = 'A+'
    B = 'B'
    B_MINUS = 'B-'
    G = 'G'
    NA = 'NA'


class District(Enum):
    Aveiro = '1'
    Beja = '2'
    Braga = '3'
    Braganca = '4'
    Castelo_Branco = '5'
    Coimbra = '6'
    Evora = '7'
    Faro = '8'
    Guarda = '9'
    Ilha_da_Graciosa = '24'
    Ilha_da_Madeira = '19'
    Ilha_das_Flores = '28'
    Ilha_de_Porto_Santo = '20'
    Ilha_de_Santa_Maria = '21'
    Ilha_de_Sao_Jorge = '25'
    Ilha_de_Sao_Miguel = '22'
    Ilha_do_Corvo = '29'
    Ilha_do_Faial = '27'
    Ilha_do_Pico = '26'
    Ilha_Terceira = '23'
    Leiria = '10'
    Lisboa = '11'
    Portalegre = '12'
    Porto = '13'
    Santarem = '14'
    Setubal = '15'
    Viana_do_Castelo = '16'
    Vila_Real = '17'
    Viseu = '18'
