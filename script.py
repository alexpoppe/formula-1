from classes import Constructor, Race, Calendar, AMERICA_BASE, ASIA_BASE
import pandas as pd
import sys
import os

# These are the indexes of all the races in a list that follows the perfect route with the least distance.
# This would be the perfect calendar based on distance.
# The calculations to find this optimal calendar can be found in "optimal_calendar.py"
PERFECT_INDEXES = [21, 5, 19, 20, 22, 9, 11, 14, 13, 15, 6, 7, 8, 10, 12, 4, 1, 18, 23, 2, 16, 17, 3]


def create_constructors() -> list:
    homebases = pd.read_csv('homebases.csv')
    
    constructors = []
    for _, row in homebases.iterrows():
        bases = {'Europe': (row.latitude, row.longitude), 'America': AMERICA_BASE, 'Asia': ASIA_BASE}
        constructor = Constructor(row.Constructor, row.Country, row.City, bases)
        constructors.append(constructor)
    return constructors

def create_races(n_hubs: int=3) -> list:
    data = pd.read_csv('races2023.csv')
    hub_column = 'hub' + str(n_hubs)
    
    races = []
    for _, row in data.iterrows():
        race = Race(row.Country, row.City, row.Latitude, row.Longitude, row[hub_column])
        races.append(race)
        
    return races

def create_calendar(races: list, constructors: list, order: list=None) -> Calendar:
    calendar = Calendar(races, constructors)
    if order:
        calendar.reorganise_races(order)
    
    return calendar

def write_data(calendar: Calendar, n_hubs: int, calendar_type: str):
    filename = calendar_type + '_calendar_' + n_hubs + 'hubs.txt'
    filepath = os.path.join('calendars', filename)
    with open(filepath, 'w') as f:
        f.write(str(calendar))

    print(f"written {calendar_type} calendar to the file {filepath}")
        
if __name__ == '__main__':
    n_hubs = sys.argv[1]
    constructors = create_constructors()
    races = create_races(n_hubs=n_hubs)
    
    current_calendar = create_calendar(races, constructors)
    write_data(current_calendar, n_hubs, calendar_type='current')
    
    optimal_calendar = create_calendar(races, constructors, order=PERFECT_INDEXES)
    write_data(optimal_calendar, n_hubs, calendar_type='optimal')