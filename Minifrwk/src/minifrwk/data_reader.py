import importlib.resources

def read_data_table():
    path = importlib.resources.files("minifrwk") / "data/tabla.csv"
    return path.read_text()    

    # # variante 2 para la misma tarea 
    # with importlib.resources.files("minifrwk") / "data/tabla.csv" as f: # type: ignore
    #     return f.read_text()