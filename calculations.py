from classes import Race, Calendar
from functions import create_calendars, plan_calendar, plan_calendars
import networkx as nx 
from networkx.algorithms import approximation as approx
import sys


def read_races():
    with open('races.txt', 'r') as f:
        text = f.readlines()
        
    races = []
    for info in text:
        info = info.strip().split(',')
        race = Race(info[0], float(info[1]), float(info[2]))
        races.append(race)
        
    return races

def write_races(calendars):
    with open('calendars.txt', 'w') as f:
        for calendar in calendars:
            f.write(str(calendar))


def manual_calculations():
    races = read_races()
    calendars = create_calendars(races)
    finished_calendars = plan_calendars(calendars)
    finished_calendars.sort(key=lambda x: x.distance)
    write_races(finished_calendars)
    print("MANUAL CALCULATIONS")
    print("Most optimal calendar:\n")
    print(finished_calendars[0])
    
    
def automatic_calculations():
    races = read_races()
    
    G = nx.Graph()
    
    for race1 in races:
        for race2 in races:
            G.add_edge(race1, race2, weight=race1.calculate_distance(race2))
    
    min_cost = float('inf')
    for race in races:
        cycle = approx.greedy_tsp(G, source=race)[:-1]
        cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
        if cost < min_cost:
            min_cycle = cycle
            min_cost = cost
            
    calendar = Calendar(min_cycle)

    print("AUTOMATIC CALCULATIONS")
    print("Most optimal calendar:\n")
    print(calendar)


if __name__ == "__main__":
    try:
        argument = sys.argv[1]
        print()
        if argument == "manual":
            manual_calculations()
        elif argument == "automatic":
            automatic_calculations()
        elif argument == "both":
            manual_calculations()
            print('------------------\n')
            automatic_calculations()
        else:
            print("Not a valid argument, choose from: 'manual', 'automatic' or 'both'")
    except IndexError as e:
        print("You didn't give an argument, choose from: 'manual', 'automatic' or 'both")
    