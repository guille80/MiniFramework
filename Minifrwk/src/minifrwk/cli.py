import typer
import yaml

app = typer.Typer()

@app.command()
def run(config: str = typer.Option(..., "--config", help="Ruta al archivo de configuración YAML")):
    """Carga y muestra el diccionario de configuración."""
    with open(config, 'r') as f:
        cfg = yaml.safe_load(f)
        typer.echo(cfg)

@app.command()
def suma(sumatoria: str = typer.Option(..., "--sumatoria", help="Ruta al archivo de configuración YAML")):
    """Suma dos números contenidos en la lista "numeros" en el archivo de configuración ."""
    with open(sumatoria, 'r') as f:
        cfg = yaml.safe_load(f)
        typer.echo(cfg)
        numeros = cfg["numeros"]
        typer.echo(f"Números a sumar: {numeros}")
        total = sum(numeros)
        typer.echo(f"La suma de los números es: {total}")

@app.command()
def suma2(config: str = typer.Option(..., "--config", help="Ruta al archivo de configuración YAML")):
    """Suma dos números contenidos en la lista "numeros" en el archivo de configuración ."""
    import json
    with open(config, 'r') as f:
        cfg = yaml.safe_load(f)
        print(json.dumps(cfg, indent=4))


if __name__ == "__main__":
    app()