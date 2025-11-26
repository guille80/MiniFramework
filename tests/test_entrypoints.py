import importlib.metadata
import pytest

def test_numeric_ops_entrypoints_resolve():
    eps = importlib.metadata.entry_points(group="minifrwk.numeric_ops")
    names = {ep.name for ep in eps}
    assert "suma" in names, "Entry point 'suma' no está definido"
    assert "reductor" in names, "Entry point 'reductor' no está definido"

    for ep in eps:
        func_or_class = ep.load()
        assert callable(func_or_class), f"Entry point {ep.name} no es ejecutable"


def test_text_ops_entrypoints_resolve():
    eps = importlib.metadata.entry_points(group="minifrwk.text_ops")
    names = {ep.name for ep in eps}
    assert "algoritmo_a" in names, "Entry point 'algoritmo_a' no está definido"

    for ep in eps:
        func_or_class = ep.load()
        assert callable(func_or_class), f"Entry point {ep.name} no es ejecutable"


def test_cli_script_resolves():
    eps = importlib.metadata.entry_points(group="console_scripts")
    ep = next((e for e in eps if e.name == "mini"), None)
    assert ep is not None, "Script 'mini' no está definido en console_scripts"
    func_or_class = ep.load()
    assert callable(func_or_class), "Script 'mini' no apunta a una función ejecutable"