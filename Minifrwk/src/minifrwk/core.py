import importlib.metadata

from .numeric_ops import *
from .text_ops import *


def cargar_numeric_ops():
    ops = {}
    # Carga dinámica de entry points registrados en minifrwk.numeric_ops
    eps = importlib.metadata.entry_points()
    for entry_point in eps.select(group="minifrwk.numeric_ops"):
        cls = entry_point.load()
        ops[entry_point.name] = cls()

    # Si se quieren agregar operaciones internas por defecto, sin instalar como paquete, descomentar lo siguiente
    # Asegurar que las operaciones internas del framework siempre estén presentes
    # if "suma" not in ops:
    #     ops["numeric_ops"] = Sumatoria()

    return ops


def cargar_text_ops():
    ops = {}
    # Carga dinámica de entry points registrados en minifrwk.text_ops
    eps = importlib.metadata.entry_points()
    for entry_point in eps.select(group="minifrwk.text_ops"):
        cls = entry_point.load()
        ops[entry_point.name] = cls()

    # Si se quieren agregar operaciones internas por defecto, sin instalar como paquete, descomentar lo siguiente
    # Asegurar que las operaciones internas del framework siempre estén presentes
    # if "text_ops" not in ops:
    #     ops["text_ops"] = Text_ops()

    return ops