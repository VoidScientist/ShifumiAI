import random as rd

from AI import AI

PLAYABLE = ["p", "f", "c"]
WIN_CASES = [["p", "f"], ["f", "c"], ["c", "p"]]
POP_SIZE = 100
ELITISM = 10
MAX_GEN = 10000
MUTATION_RATE = 0.15
TOURNAMENT_SIZE = 5
TEST_ROUNDS = 10
STRATEGIES_NUMBER = 4
CHOICES_NUMBER = 3


def create_genes():
    return [[rd.random() for i in range(STRATEGIES_NUMBER)],
            [rd.random() for i in range(CHOICES_NUMBER)]]


population = [AI(create_genes()) for i in range(POP_SIZE)]
ranked_population = []


def determine_winner(player, ai):
    if [ai, player] in WIN_CASES:
        return 1
    if ai == player:
        return 0.5
    return 0


def evaluate(ind):
    fitness = 0
    for i in range(TEST_ROUNDS):
        player = AI([[rd.random()] * STRATEGIES_NUMBER, [rd.random()] * CHOICES_NUMBER])
        player_action = player.act()
        fitness += determine_winner(ind.act(), player_action)
        ind.last_player_action = player_action
    return fitness


def mutate(arg):
    for i in range(len(arg)):
        if rd.random() < MUTATION_RATE:
            arg[i] = rd.random()


def tournament(pop):
    return sorted(pop, key=evaluate, reverse=True)[:2]


for gen in range(MAX_GEN):
    ranked_population = sorted(population, key=evaluate, reverse=True)

    parent1, parent2 = tournament(rd.sample(ranked_population, TOURNAMENT_SIZE))

    population = []
    population += ranked_population[:ELITISM + 1]
    for _ in range(POP_SIZE - ELITISM):
        p1_inheritance = rd.randrange(1, STRATEGIES_NUMBER - 1)
        child_action_genes = rd.sample(parent1.genes[0], p1_inheritance) + rd.sample(parent1.genes[0],
                                                                                     STRATEGIES_NUMBER - p1_inheritance)
        p2_inheritance = rd.randrange(1, CHOICES_NUMBER - 1)
        child_choice_genes = rd.sample(parent2.genes[1], p2_inheritance) + rd.sample(parent1.genes[1],
                                                                                     CHOICES_NUMBER - p2_inheritance)
        mutate(child_action_genes)
        mutate(child_choice_genes)

        population.append(AI([child_action_genes, child_choice_genes]))

print(f"Win percentage : {(evaluate(ranked_population[0]) / TEST_ROUNDS) * 100}%")
print(ranked_population[0].genes)
