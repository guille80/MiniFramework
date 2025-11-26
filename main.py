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

    try:
        # Cargar y usar un plugin específico mediante load_plugin (usando instanciación directa)
        # reductor_plugin = load_plugin("reductor")
        
        # o usando factory_plugin (usando patrón fábrica)
        reductor_class = factory_plugin("reductora")
        reductor_plugin = reductor_class([1000])  # Inicializa con un total de 1000

        resultado_reductor = reductor_plugin.run([10, 20, 30, 40])
        print("Resultado del reductor:", resultado_reductor)
    except ValueError as e:
        print(e)

    # carga directa del plugin sin usar entry points
    try:
        # o usando factory_plugin (usando patrón fábrica)
        reductor2 = factory_plugin("minifrwk.numeric_ops.resta:Reductor")
        reductor_plugin2 = reductor2([1000])  # Inicializa con un total de 1000

        resultado_reductor2 = reductor_plugin2.run([10, 20, 30, 40])
        print("Resultado del reductor:", resultado_reductor2)
    except ValueError as e:
        print(e)

    # carga directa de una función sin usar entry points
    try:
        # o usando factory_plugin (usando patrón fábrica)
        reductor3 = factory_plugin("minifrwk.numeric_ops.resta:resta")
        reductor_plugin3 = reductor3(1000, 444)  # Inicializa con un total de 1000

        # resultado_reductor3 = reductor_plugin3.run([10, 20, 30, 40])
        print("Resultado de la resta:", reductor_plugin3)
    except ValueError as e:
        print(e)

    print("Ejecución completada. versión de Minifrwk:", minifrwk.__version__)

if __name__ == "__main__":
    main()