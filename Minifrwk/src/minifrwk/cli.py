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

@app.command()
def validate1(config: str = typer.Option(..., "--config", help="Ruta al archivo de configuración YAML")):
    """Valida tipos en el archivo de configuración YAML."""
    from minifrwk.config_loader.loader import load_yaml, print_validation_result

    data = load_yaml(config)
    print("Datos cargados desde YAML:", data)

    print("Validando tipos YAML:")

    print_validation_result('seed', data['seed'], 'int')
    print_validation_result('rounds', data['rounds'], 'int')
    print_validation_result('round_name', data['round_name'], 'int')
    print_validation_result('clients', data['clients'], 'dict')
    print_validation_result('clients.total', data['clients']['total'], 'int')
    print_validation_result('clients.per_round', data['clients']['per_round'], 'int')
    print_validation_result('clients.lr', data['clients']['lr'], 'float')
    print_validation_result('algorithm', data['algorithm'], 'dict')

@app.command()
def validate(config: str = typer.Option(..., "--config", help="Ruta al archivo de configuración YAML")):
    """Valida tipos en el archivo de configuración YAML."""
    from minifrwk.config_loader.loader import load_yaml, print_validation_result

    data = load_yaml(config)
    with open(config, 'r') as f:
        cfg = yaml.safe_load(f)
        faltantes = []
        obligatorios = ["seed", "rounds", "clients", "algorithm", "logging", "data"]
        for campo in obligatorios:
            if campo not in cfg:
                faltantes.append(campo)
        if faltantes:
            typer.echo(f"Faltan campos obligatorios: {', '.join(faltantes)}")
            raise typer.Exit(code=1)
        else:
            typer.echo("Todos los campos obligatorios están presentes.")

        
if __name__ == "__main__":
    app()