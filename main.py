from Minifrwk import *
from Minifrwk.src.minifrwk import *
import minifrwk
# from Minifrwk.src.minifrwk import MiniFrwk # no funciona
# from Minifrwk.src.minifrwk import cargar_numeric_ops, cargar_text_ops

def main():

    # Inicializar el framework
    minifrwk.load_config_yaml()

    # Cargar operaciones numéricas y de texto
    numeric_ops = cargar_numeric_ops()
    text_ops = cargar_text_ops()
    print("Plugins numéricos cargados:", list(numeric_ops.keys()))
    print("Plugins de texto cargados:", list(text_ops.keys()))

    # Ejemplo de uso de operaciones numéricas
    numeros = [4, 5]
    if "numeric_plugin" in numeric_ops:
        potencia = numeric_ops["numeric_plugin"].run(numeros)
        print("Potencia:",numeros, potencia)

    if "potencia" in numeric_ops:
        potencia = numeric_ops["potencia"].run(numeros)
        print("Potencia2:",numeros, potencia)

    if "suma" in numeric_ops:
        suma_total = numeric_ops["suma"].run(numeros)
        print("Suma total:", suma_total)

    # Ejemplo de uso de operaciones de texto
    textos = ["hola", "mundo", "python"]
    if "text_plugin" in text_ops:
        resultados_invertidos = [text_ops["text_plugin"].run(t) for t in textos]
        print("Textos invertidos:", resultados_invertidos)

    if "algoritmo_a" in text_ops:
        textos_mayusculas = text_ops["algoritmo_a"].run(textos)
        print("Textos en mayúsculas:", textos_mayusculas)

    read_data = minifrwk.read_data_table()
    print("Datos leídos desde el archivo:", read_data)

    listar_entry_points_by_group("minifrwk.numeric_ops")
    listar_entry_points_by_group("minifrwk.text_ops") 

    print("Ejecución completada. versión de Minifrwk:", minifrwk.__version__)

if __name__ == "__main__":
    main()