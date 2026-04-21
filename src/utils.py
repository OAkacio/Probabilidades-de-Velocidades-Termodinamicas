#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from astropy import constants as cons
import numpy as np

#! -------------------------------------------------- Constantes Físicas --------------------------------------------------
R = cons.R.value * 1000 # Multiplicado por 1000 para passar a massa molar utilizada ser em gramas por mol.
zero_abs = -273.15
pi = np.pi
e = np.e


#! -------------------------------------------------- Funções de Conversão --------------------------------------------------
def CelsiusToKelvin(T):
    return T - zero_abs
