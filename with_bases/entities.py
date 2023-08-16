from geopy.distance import geodesic

class Constructor:
    def __init__(self, name: str, country: str, city: str, bases: dict) -> None:
        self.name = name
        self.country = country
        self.city = city
        self.bases = bases
        self.total_distance = None
        
    def calculate_distance(self, race1: "Race", race2: "Race") -> float:
        if not race1:
            coords_1 = self.bases[race2.location_group]
            coords_2 = (race2.latitude, race2.longitude)
            distance = geodesic(coords_1, coords_2).km
            return distance
        
        if not race2:
            coords_1 = (race1.latitude, race1.longitude)
            coords_2 = self.bases[race1.location_group]
            distance = geodesic(coords_1, coords_2).km
            return distance

        coords_1 = (race1.latitude, race1.longitude)
        coords_2 = (race2.latitude, race2.longitude)
        
        if race1.location_group == race2.location_group:
            distance = geodesic(coords_1, coords_2).km
        else:
            base_1 = self.bases[race1.location_group]
            distance = geodesic(coords_1, base_1).km
            
            base_2 = self.bases[race2.location_group]
            distance += geodesic(base_2, coords_2).km
        return distance
    
    def calculate_distance_nohubs(self, race1: "Race", race2: "Race"):
        if not race1:
            coords_1 = self.bases["Europe"]
            coords_2 = (race2.latitude, race2.longitude)
            distance = geodesic(coords_1, coords_2).km
            return distance
        
        if not race2:
            coords_1 = (race1.latitude, race1.longitude)
            coords_2 = self.bases["Europe"]
            distance = geodesic(coords_1, coords_2).km
            return distance
        
        coords_1 = (race1.latitude, race1.longitude)
        coords_2 = (race2.latitude, race2.longitude)
        
        distance = geodesic(coords_1, coords_2).km
        return distance
            
    
    def calculate_calendar(self, races: list) -> float:
        distance = self.calculate_distance(None, races[0])
        
        for i in range(len(races) - 1):
            race1 = races[i]
            race2 = races[i+1]
            distance += self.calculate_distance(race1, race2)
            
        distance += self.calculate_distance(races[-1], None)
        self.total_distance = distance
    
        return distance
    
    def __repr__(self) -> str:
        return f"{self.name}: {self.country}, {self.city} ({self.total_distance} km)\n"
    
class Race:
    def __init__(self, country: str, city: str, latitude: float, longitude: float, location_group: str) -> None:
        self.country = country
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.location_group = location_group
        self.id = None
        
    def __repr__(self) -> str:
        value = ""
        if self.id:
            value += f"{self.id}. "
        
        return value + f"{self.country} ({self.city}) -> {self.location_group}"


class Calendar:
    def __init__(self, races: list, constructors: list) -> None:
        self.races = races
        self.constructors = constructors
        
        for index, race in enumerate(self.races):
            race.id = index + 1
        
        self.total_distance = self.calculate_distance()
        
    def calculate_distance(self) -> float:
        total_distance = 0
        for constructor in self.constructors:
            total_distance += constructor.calculate_calendar(self.races)
            
        return total_distance
        
    def reorganise_races(self, indexes: list) -> list:
        self.new_races = []
        for index in indexes:
            for race in self.races:
                if race.id == index:
                    self.new_races.append(race)
                    break
                
        self.races = self.new_races
        self.total_distance = self.calculate_distance()
        return self.races
    
    def __repr__(self) -> str:
        value = "Calendar\n"
        for race in self.races:
            value += f"\t{race}\n"
        value += f"total distance: {self.total_distance} km\n\n"
        
        for constructor in self.constructors:
            value += str(constructor)
        
        return value
        
        
        
                