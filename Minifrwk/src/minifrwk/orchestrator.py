import yaml
from minifrwk.core import load_algorithm
from minifrwk.sample import sample_clients

def run(cfg):
    # 1. Cargar configuración si es ruta a YAML
    if isinstance(cfg, str):
        with open(cfg, 'r') as f:
            cfg = yaml.safe_load(f)

    # 2. Cargar clase de algoritmo
    Alg = load_algorithm(cfg["algorithm"]["id"])
    alg = Alg(cfg)

    # 3. Inicializar estado global
    w_t = 0  # O adaptar según necesidad
    history = [w_t]

    total = cfg["clients"]["total"]
    per_round = cfg["clients"]["per_round"]
    seed = cfg["seed"]
    rounds = cfg["rounds"]
    
    for t in range(rounds):
        # 4a. Seleccionar clientes
        client_ids = sample_clients(total, per_round, seed, t)

        # 4b. Actualizaciones de clientes
        updates = [alg.client_update(w_t, cid) for cid in client_ids]

        # 4c. Agregación
        w_t = alg.aggregate(w_t, updates)
        history.append(w_t)
        print(f"Ronda {t}: estado = {w_t}")
    return history

""" import random

def sample_clients(total, per_round, seed, round_idx):
    rng = random.Random(seed + round_idx)
    return rng.sample(range(total), per_round)


def run_simulation(num_rounds, total_clients, clients_per_round, seed):
    for round_idx in range(num_rounds):
        clients = sample_clients(total_clients, clients_per_round, seed, round_idx)
        print(f"Round {round_idx + 1}: Selected clients: {clients}") """