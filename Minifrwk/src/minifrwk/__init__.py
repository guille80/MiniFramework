from .numeric_ops.resta import resta
from .numeric_ops.suma import suma, Sumatoria
from .data_reader import read_data_table
from .core import cargar_numeric_ops, cargar_text_ops, listar_entry_points_by_group
from .config_loader.loader import load_config_yaml


__all__ = ["cargar_numeric_ops", "cargar_text_ops", 'suma', 'resta', 'Sumatoria',
           "read_data_table", "load_config_yaml", 'listar_entry_points_by_group']

from importlib.metadata import version, PackageNotFoundError
try:
    __version__ = version("minifrwk")
except PackageNotFoundError:
    __version__ = "unknown"

def __getattr__(name):
    if name == "core":
        # Solo se importa cuando alguien realmente usa minifrwk.core
        import minifrwk.core as mod
        return mod
    raise AttributeError(f"module {__name__} has no attribute {name}")