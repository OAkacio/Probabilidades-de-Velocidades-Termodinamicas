#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from src.parameters import *
from src.utils import *


#! -------------------------------------------------- Funções Principais --------------------------------------------------
def MaxwellBoltzmann(v):
    x = (
        4
        * (pi)
        * ((M / (2 * (pi) * R * T)) ** (3 / 2))
        * (v**2)
        * (e) ** ((-M * v ** (2)) / (2 * R * T))
    )
    return x


def V_MaisProvavel(T, M):
    return ((2 * R * T) / (M)) ** (1 / 2)


def V_Media(T, M):
    return ((8 * R * T) / (pi * M)) ** (1 / 2)


def V_RMS(T, M):
    return ((3 * R * T) / (M)) ** (1 / 2)
