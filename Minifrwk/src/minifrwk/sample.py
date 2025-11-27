import random

def sample_clients(total, per_round, seed, round_idx):
    rng = random.Random(seed + round_idx)
    return rng.sample(range(total), per_round)