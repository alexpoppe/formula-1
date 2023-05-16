
from geopy.distance import geodesic

        
class Race:
    def __init__(self, name: str, latitude: float, longitude: float) -> None:
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        
    def calculate_distance(self, race: "Race") -> int:
        coords_1 = (self.latitude, self.longitude)
        coords_2 = (race.latitude, race.longitude)

        return geodesic(coords_1, coords_2).km
    
    def closest(self, races: list) -> "Race":
        shortest_distance = float('inf')
        for race in races:
            distance = self.calculate_distance(race)
            if distance < shortest_distance:
                shortest_distance = distance
                closest_race = race
                
        return closest_race
    
    
    def __repr__(self) -> str:
        return f"Race {self.name} {self.latitude, self.longitude}"
                

        
class Calendar:
    def __init__(self, races: list=[], to_plan: list=[]) -> None:
        self.races = races
        self.to_plan = to_plan
        self.distance = 0
        if races:
            _ = self.calculate_distance()
        
        
        
    def add_race(self, race: Race) -> list:
        if self.races:
            distance = self.races[-1].calculate_distance(race)
            self.distance += distance
            
        self.races.append(race)
        
        if self.to_plan:
            self.to_plan.remove(race)
        
        return self.races
        
    def pop_race(self) -> list:
        distance = self.races[-2].calculate_distance(self.races[-1])
        self.distance -= distance
        race = self.races.pop()
        return race
    
    def remove_race(self, race: Race) -> list:
        self.races.remove(race)
        self.calculate_distance()
        return self.races
    
    def remove_index(self, index: int) -> Race:
        race = self.races.pop(index)
        self.calculate_distance()
        return race
    
    def calculate_distance(self) -> int:
        total_distance = 0
        for index in range(len(self.races) - 1):
            race1 = self.races[index]
            race2 = self.races[index + 1]
            
            distance = race1.calculate_distance(race2)
            total_distance += distance
        
        self.distance = total_distance
        return total_distance
    
    def __repr__(self) -> str:
        result = "Calendar\n"
        for race in self.races:
            result += "\t"
            result += str(race)
            result += "\n"
        
        result += f"distance: {round(self.distance, 2)} km\n\n"
        
        if self.to_plan:
            result += "to plan: "
            result += str(self.to_plan)
            result += "\n\n"
        return result
            
