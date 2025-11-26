import importlib.metadata
import importlib

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

def get_entry_points_by_group(group_name):
    python_version = get_python_version()
    if python_version.startswith("3.8") or python_version.startswith("3.9"):
        return importlib.metadata.entry_points().get(group_name, [])
    else:
        return importlib.metadata.entry_points(group=group_name)

import sys

def get_python_version() -> str:
    """
    Devuelve la versión de Python en formato 'mayor.menor.micro'.
    """
    version_info = sys.version_info
    return f"{version_info.major}.{version_info.minor}.{version_info.micro}"


def load_plugin(plugin_id: str):
    """
    Carga un plugin basado en su ID desde los entry points registrados.
    Devuelve una instancia del plugin si se encuentra, de lo contrario lanza un ValueError
    """
    # obtiene los entry points de ambos grupos
    eps = get_entry_points_by_group("minifrwk.numeric_ops") + get_entry_points_by_group("minifrwk.text_ops")
    for entry_point in eps:
        if entry_point.name == plugin_id:
            cls = entry_point.load()
            return cls()
    
    raise ValueError(f"Plugin con ID '{plugin_id}' no encontrado.")

def factory_plugin(plugin_id: str):
    """
    Fábrica para crear instancias de plugins basados en su ID.
    """
    eps = get_entry_points_by_group("minifrwk.numeric_ops") + get_entry_points_by_group("minifrwk.text_ops")
    # Buscar el entry point por nombre
    for entry_point in eps:
        if entry_point.name == plugin_id:
            # Importar y devolver la clase usando la ruta registrada
            module, class_name = entry_point.value.split(":")
            mod = importlib.import_module(module)
            return getattr(mod, class_name)
    # Si no se encuentra en los entry points, intentar cargar directamente
    if ":" in plugin_id:
        module, class_name = plugin_id.split(":")
        mod = importlib.import_module(module)
        return getattr(mod, class_name)

    raise ValueError(f"Plugin con ID '{plugin_id}' no encontrado.")

# Fábrica para cargar algoritmos por su ID.
def load_algorithm(algorithm: str):
    """
    Fábrica para cargar algoritmos por su ID.
    """
    eps = get_entry_points_by_group("minifrwk.algorithms")
    # Buscar el entry point por nombre
    for entry_point in eps:
        if entry_point.name == algorithm:
            # Importar y devolver la clase usando la ruta registrada
            module, class_name = entry_point.value.split(":")
            mod = importlib.import_module(module)
            return getattr(mod, class_name)
    # Si no se encuentra en los entry points, intentar cargar directamente
    if ":" in algorithm:
        module, class_name = algorithm.split(":")
        mod = importlib.import_module(module)
        return getattr(mod, class_name)

    raise ValueError(f"Plugin con ID '{algorithm}' no encontrado.")