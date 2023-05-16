from classes import Calendar, Race
import copy

def create_calendars(races: list) -> list:
    calendars = []
    for index in range(len(races)):
        to_plan = races[:index] + races[index+1:]
        calendar = Calendar(races=[races[index]], to_plan=to_plan)
        calendars.append(calendar)
        
    return calendars

def plan_calendar(calendar: Calendar) -> None:
    while calendar.to_plan:
        last_race = calendar.races[-1]
        
        closest_race = last_race.closest(calendar.to_plan)
        calendar.add_race(closest_race)
    
    return None

def plan_calendars(calendars: list) -> list:
    finished_calendars = []
    
    for calendar in calendars:
        plan_calendar(calendar)
        finished_calendars.append(calendar)
        
    return finished_calendars


def plan_calendar_double(calendar: Calendar) -> list:
    new_calendars = []
    while len(calendar.to_plan) > 1:
        races = [race for race in calendar.races]
        to_plan = [race for race in calendar.to_plan]
        new_calendar = Calendar(races, to_plan)
        last_race = calendar.races[-1]
        
        closest_race = last_race.closest(calendar.to_plan)
        calendar.add_race(closest_race)
        second_closest_race = last_race.closest(calendar.to_plan)
        new_calendar.add_race(second_closest_race)
        new_calendars.append(new_calendar)
        
    calendar.add_race(calendar.to_plan[0])
        
    return new_calendars