#
#! -------------------------------------------------- Bibliotecas --------------------------------------------------
from src.core import *
from src.parameters import *
from src.utils import *
import numpy as np

#! -------------------------------------------------- Início da Rotina Principal --------------------------------------------------


def main():
    print(
        "\n Iniciando o programa de distribuição de velocidades de Maxwell-Boltzmann \n"
    )
    print("-" * 100)
    try:  # * Calcula os pontos no gráfico e a distribuição de velocidades
        vectorX = []
        vectorY = []
        vector_car = []
        for i in range(0, int(VELOCIDADE_MAXIMA_DE_OUTPUT), int(STEPS)):
            vectorX.append(i)
            vectorY.append(MaxwellBoltzmann(i))
        v_mp = V_MaisProvavel(T, M)
        vector_car.append(v_mp)
        v_avg = V_Media(T, M)
        vector_car.append(v_avg)
        V_rms = V_RMS(T, M)
        vector_car.append(V_rms)
        breakp = 0
        print("\n Pontos do gráfico gerados com sucesso! \n")
        print("-" * 100)
    except:
        breakp = 1
        print(
            "\n Houve um erro na geração dos pontos do gráfico. Verifique os parâmetros de entrada e tente novamente. \n"
        )
        print("-" * 100)
    if breakp == 0:
        try:  # * Salva dados gerados em arquivos .txt
            print("\n Salvando os dados gerados da distribuição de velocidades... \n")
            print("-" * 100)
            data = np.column_stack((vectorX, vectorY))
            header_text = (
                "Descripiton: Distribuicao da Velocidades de Maxwell-Boltzmann\n"
                "Author: Victor Moreira Acacio \n"
                "\n"
                "Equation: 4 * pi * (M / (2 * pi * R * T))^(3/2) * v^2 * exp(-M * v^2 / (2 * R * T))\n"
                f"Domain: v em [0, {VELOCIDADE_MAXIMA_DE_OUTPUT}]\n"
                "Units: v [m/s], f(v) [s/m] \n"
                "\n"
                f"Temperature: {T} K\n"
                f"Most Probable Velocity (v_mp): {v_mp:.2f} m/s\n"
                f"Mean Velocity (v_avg): {v_avg:.2f} m/s \n"
                f"Root Mean Square Velocity (V_rms): {V_rms:.2f} m/s \n"
                "\n"
                "v,f(v)"
            )
            np.savetxt(
                "data/dados.txt",
                data,
                fmt="%.6f",
                delimiter=",",
                header=header_text,
                comments="# ",
            )
            print("\n Arquivo 'dados.txt' gerado com sucesso! \n")
            print("-" * 100)
            print(
                "\n Salvando os dados caracterrísticos da distribuição de velocidades... \n"
            )
            print("-" * 100)
            data_car = np.column_stack((vector_car, (0, 0, 0)))
            header_text = (
                "Descripiton: Velocidades Caracteristicas da Distribuicao da Velocidades de Maxwell-Boltzmann\n"
                "Author: Victor Moreira Acacio \n"
                "\n"
                "Equations: v_mp = ((2 * R * T) / (M)) ** (1 / 2)\n     v_med = ((8 * R * T) / (pi * M)) ** (1 / 2)\n     v_rms = ((3 * R * T) / (M)) ** (1 / 2)\n"
                "Units: v [m/s]\n"
                f"Temperature: {T} K\n"
                "\n"
                "v,---"
            )
            np.savetxt(
                "data/dados_car.txt",
                data_car,
                fmt="%.6f",
                delimiter=",",
                header=header_text,
                comments="# ",
            )
            print("\n Arquivo 'dados_car.txt' gerado com sucesso! \n")
            print("-" * 100)
        except:
            print("\n Houve um erro ao salvar os dados. \n")
            print("-" * 100)
    print("\n Distribuição de Velocidades de Maxwell-Boltzmann FINALIZADA! \n")
    print("-" * 100)


if __name__ == "__main__":
    main()
