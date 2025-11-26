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

def listar_entry_points():
    numeric_ops = []
    text_ops = []

    eps = importlib.metadata.entry_points()

    for entry_point in eps.select(group="minifrwk.numeric_ops"):
        numeric_ops.append(entry_point.name)

    for entry_point in eps.select(group="minifrwk.text_ops"):
        text_ops.append(entry_point.name)

    return numeric_ops, text_ops

def listar_entry_points_by_group(group_name):
    python_version = get_python_version()
    if python_version.startswith("3.8") or python_version.startswith("3.9"):
        eps = importlib.metadata.entry_points().get(group_name, [])
    else:
        eps = importlib.metadata.entry_points(group=group_name)
    for entry_point in eps:
        print(f"Entry Point: {entry_point.name}, Module: {entry_point.module}, Object: {entry_point.value}") 

import sys

def get_python_version() -> str:
    """
    Devuelve la versión de Python en formato 'mayor.menor.micro'.
    """
    version_info = sys.version_info
    return f"{version_info.major}.{version_info.minor}.{version_info.micro}"