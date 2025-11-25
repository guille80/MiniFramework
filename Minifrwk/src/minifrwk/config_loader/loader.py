import yaml

def load_yaml(file_path):
    """
    Carga un archivo YAML y retorna su contenido como un diccionario de Python.
    Parámetros:
        file_path: ruta al archivo YAML
    Retorna:
        dict: contenido del archivo YAML
    """
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def validar_tipo_yaml(valor, tipo_str):
    """
    Valida si un valor corresponde al tipo YAML especificado.
    
    Parámetros:
        valor: cualquier dato a validar
        tipo_str: nombre del tipo en string (ej. 'int', 'str', 'list')
    
    Retorna:
        True si el valor es del tipo especificado, False en caso contrario.
    """
    tipos_yaml = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "null": type(None),
        "list": list,
        "dict": dict,
    }
    
    if tipo_str not in tipos_yaml:
        raise ValueError(f"Tipo '{tipo_str}' no soportado en YAML")
    
    return isinstance(valor, tipos_yaml[tipo_str])

def print_validation_result(name, value, type):
    result = "OK" if validar_tipo_yaml(value, type) else "FAIL"
    print(f"Validando {type} en '{name}'--> {result}, valor: {value}")

# Ejemplo de uso:
def load_config_yaml() :

    data = load_yaml("config.yaml")
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
    print_validation_result('algorithm.id', data['algorithm']['id'], 'str')
    print_validation_result('algorithm.params', data['algorithm']['params'], 'dict')
    print_validation_result('logging.level', data['logging']['level'], 'str')   
    print_validation_result('logging.output_dir', data['logging']['output_dir'], 'str')   
    return data
