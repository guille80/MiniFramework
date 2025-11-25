from .numeric_ops.resta import resta
from .numeric_ops.suma import suma, Sumatoria
from .core import cargar_numeric_ops, cargar_text_ops

__all__ = ["cargar_numeric_ops", "cargar_text_ops", 'suma', 'resta', 'Sumatoria']

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