import networkx as nx
from classes import Race
import pandas as pd
from networkx.algorithms import approximation as approx


def create_races(n_hubs: int=3) -> list:
    data = pd.read_csv('races2023.csv')
    hub_column = 'hub' + str(n_hubs)
    
    races = []
    for index, row in data.iterrows():
        race = Race(row.Country, row.City, row.Latitude, row.Longitude, row[hub_column])
        race.id = index + 1
        races.append(race)
        
    return races

def create_graph(races: list):
    G = nx.Graph()
    
    for race1 in races:
        for race2 in races:
            if race1 != race2:
                G.add_edge(race1, race2, weight=race1.calculate_distance(race2))
    return G
    
def calculate_optimal(graph, races: list):
    min_cost = float("inf")
    for race in races:
        cycle = approx.greedy_tsp(graph, source=race)[:-1]
        cost = sum(graph[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
        if cost < min_cost:
            min_cycle = cycle
            min_cost = cost
    return min_cycle, min_cost


if __name__ == "__main__":
    races = create_races(n_hubs=1)
    graph = create_graph(races)
    min_cycle, min_cost = calculate_optimal(graph, races)
    print(min_cycle, min_cost)
    indexes = [race.id for race in min_cycle]
    print('PERFECT INDEXES: ', indexes)