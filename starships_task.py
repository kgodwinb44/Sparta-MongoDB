import pymongo
import requests

# MongoDB db
client = pymongo.MongoClient()
db = client['startwars']
starship_collection = db['starships']

# Get starships data and insert into collection
# def get_starships():
#     starships = requests.get("https://swapi.info/api/starships").json().get("results", [])
#     for starship in starships:
#         starship_collection.insert_one(starship)

# Get pilot names from starship
def get_ship_pilot():
    ship_pilot_name = {}
    for ship in starship_collection.find():
        pilots = ship.get("pilots")
        pilot_names = []
        for pilot_url in pilots:
            name = requests.get(pilot_url).json().get("name")
            pilot_names.append(name)
        ship_pilot_name[ship["name"]] = pilot_names
    return ship_pilot_name

# Convert name to object_id
def pilot_to_id():
    ship_pilot_id = {}
    for ship, pilot_names in get_ship_pilot().items():
        pilot_ids = []

        for name in pilot_names:
            character = db.characters.find_one({"name": name})
            if character:
                pilot_ids.append(character["_id"])
            else:
                print("not found")
        ship_pilot_id[ship] = pilot_ids
    return ship_pilot_id

def main():
    pilot_object = pilot_to_id()
    for ship_name, pilot_id in pilot_object.items():
        db.starships.update_one({"name": ship_name},
                   {"$set": {"pilots": pilot_id}}, upsert=True)
if __name__ == "__main__":
    main()






