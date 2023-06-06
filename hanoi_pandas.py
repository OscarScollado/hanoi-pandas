import pandas as pd


def mover_pieza(torres, desde, hasta):
    """
    Mueve una pieza desde una posición hasta el objetivo
    :param torres: La matriz de torres
    :param desde: Posición inicial
    :param hasta: Posición final
    :return: None
    """
    pieza_movida = torres[desde][-1]
    if len(torres[hasta]) != 0 and pieza_movida > torres[hasta][-1]:
        print(f"Movimiento ilegal. ({desde} -> {hasta})")
        return
    torres[hasta].append(torres[desde].pop(-1))


def obtener_paso(inicio, objetivo):
    """
    Obtiene la posición que debe servir como auxiliar en este caso (el "paso").
    Se obtiene simplemente descartando de las tres cuál posición es la inicial y cuál es la objetivo
    :param inicio: Posición inicial
    :param objetivo: Posición final
    :return: Posición auxiliar
    """
    return ({0, 1, 2} - {inicio, objetivo}).pop()


def resolver(torres, n, inicio, objetivo):
    """
    Resuelve las torres de hanoi para n piezas
    :param torres: La matriz de torres
    :param n: Número de piezas
    :param inicio: Posición inicial
    :param objetivo: Posición final
    :return: None
    """
    if n <= 1:
        mover_pieza(torres, inicio, objetivo)
    else:
        paso = obtener_paso(inicio, objetivo)
        resolver(torres, n - 1, inicio, paso)
        mover_pieza(torres, inicio, objetivo)
        resolver(torres, n - 1, paso, objetivo)


def generar_torres(n, inicio):
    """
    Genera la matriz de torres
    :param n: Número de piezas
    :param inicio: La posición inicial
    :return: La matriz de torres
    """
    torres = [[], [], []]
    torres[inicio] = list(range(n, 0, -1))
    return torres


def mostrar_torres(torres, num_pisos):
    """
    Muestra las torres de una manera organizada con la librería Pandas
    :param torres: La matriz de torres
    :param num_pisos: El número de piezas
    :return: None
    """
    df = pd.DataFrame(torres, dtype="float").transpose()
    df = df.rename(columns=lambda x: x + 1)
    df = df.fillna('x')
    df = df.reindex(range(num_pisos - 1, -1, -1), fill_value='x')
    print(df)
    # print(df.to_string(index=False))  # quita los índices de las filas, pero quita las tabulaciones
    print()


def main():
    pd.options.display.float_format = '{:,.0f}'.format  # para que los números se muestren sin decimal

    num_pisos = 5  # número de piezas
    inicio = 0  # posición inicial
    final = 2  # posición final

    torres = generar_torres(num_pisos, inicio)
    mostrar_torres(torres, num_pisos)
    resolver(torres, num_pisos, inicio, final)
    mostrar_torres(torres, num_pisos)


if __name__ == "__main__":
    main()