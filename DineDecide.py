# DineDecide - A Python Restaurant Decision Helper

import random

print("Welcome to DineDecide!")


# Restaurant data
restaurants = [
    {
        "name": "Sixpenny",
        "cuisine": "Modern Australian",
        "location": "Stanmore",
        "rating": 19
    },
    {
        "name": "ARIA Sydney",
        "cuisine": "Modern Australian",
        "location": "Circular Quay",
        "rating": 18
    },
    {
        "name": "Bentley Restaurant & Bar",
        "cuisine": "European",
        "location": "Sydney CBD",
        "rating": 18
    },
    {
        "name": "LuMi Bar & Dining",
        "cuisine": "Italian",
        "location": "Pyrmont",
        "rating": 17
    },
    {
        "name": "Saint Peter",
        "cuisine": "Modern Australian",
        "location": "Paddington",
        "rating": 17
    },
    {
        "name": "Berowra Waters Inn",
        "cuisine": "Modern Australian",
        "location": "Berowra Waters",
        "rating": 17
    },
    {
        "name": "Bennelong",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 17
    },
    {
        "name": "Ormeggio at The Spit",
        "cuisine": "Italian",
        "location": "Mosman",
        "rating": 16
    },
    {
        "name": "Yellow",
        "cuisine": "Vegetarian",
        "location": "Potts Point",
        "rating": 16
    },
    {
        "name": "Yoshii's Omakase",
        "cuisine": "Japanese",
        "location": "Barangaroo",
        "rating": 16
    },
    {
        "name": "Pilu At Freshwater",
        "cuisine": "Italian",
        "location": "Freshwater",
        "rating": 16
    },
    {
        "name": "Nel Restaurant",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 16
    },
    {
        "name": "Haco",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 15
    },
    {
        "name": "Bathers' Pavilion Restaurant",
        "cuisine": "Modern Australian",
        "location": "Mosman",
        "rating": 15
    },
    {
        "name": "Kuro Bar & Dining",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 15
    },
    {
        "name": "Allta",
        "cuisine": "Korean",
        "location": "Surry Hills",
        "rating": 15
    },
    {
        "name": "AMARA",
        "cuisine": "Modern Australian",
        "location": "Bowen Mountain",
        "rating": 15
    },
    {
        "name": "Oborozuki",
        "cuisine": "Fusion",
        "location": "Sydney CBD",
        "rating": 15
    },
    {
        "name": "Mimi's",
        "cuisine": "Modern Australian",
        "location": "Coogee",
        "rating": 15
    },
    {
        "name": "Firedoor",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 15
    },
    {
        "name": "AALIA",
        "cuisine": "Middle Eastern",
        "location": "Sydney CBD",
        "rating": 15
    },
    {
        "name": "Catalina Restaurant",
        "cuisine": "Modern Australian",
        "location": "Rose Bay",
        "rating": 15
    },
    {
        "name": "Gildas",
        "cuisine": "Spanish",
        "location": "Surry Hills",
        "rating": 14
    },
    {
        "name": "Restaurant Ka",
        "cuisine": "Modern Australian",
        "location": "Darlinghurst",
        "rating": 14
    },
    {
        "name": "Restaurant Moon",
        "cuisine": "Thai",
        "location": "Darlinghurst",
        "rating": 14
    },
    {
        "name": "Sushi Oe",
        "cuisine": "Japanese",
        "location": "Glebe",
        "rating": 14
    },
    {
        "name": "Restaurant Garaku",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 14
    },
    {
        "name": "Prefecture 48",
        "cuisine": "Japanese",
        "location": "East Sydney",
        "rating": 14
    },
    {
        "name": "Franca Brasserie",
        "cuisine": "Mediterranean",
        "location": "Potts Point",
        "rating": 14
    },
    {
        "name": "Ester Restaurant and Bar",
        "cuisine": "Italian",
        "location": "Chippendale",
        "rating": 14
    },
    {
        "name": "Atelier By Sofitel",
        "cuisine": "French",
        "location": "Sydney CBD",
        "rating": 14
    },
    {
        "name": "White Horse",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 14
    },
    {
        "name": "Lana",
        "cuisine": "Italian",
        "location": "Sydney CBD",
        "rating": 14
    },
    {
        "name": "Margaret",
        "cuisine": "Modern Australian",
        "location": "Double Bay",
        "rating": 14
    },
    {
        "name": "Matkim",
        "cuisine": "Korean",
        "location": "Sydney CBD",
        "rating": 14
    },
    {
        "name": "Civico 47",
        "cuisine": "Italian",
        "location": "Paddington",
        "rating": 13
    },
    {
        "name": "Carte",
        "cuisine": "European",
        "location": "Glebe",
        "rating": 13
    },
    {
        "name": "10 William Street",
        "cuisine": "Italian",
        "location": "Paddington",
        "rating": 13
    },
    {
        "name": "Morena",
        "cuisine": "Modern Australian",
        "location": "East Sydney",
        "rating": 13
    },
    {
        "name": "Porcine",
        "cuisine": "French",
        "location": "Paddington",
        "rating": 13
    },
    {
        "name": "Nour",
        "cuisine": "Lebanese",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "L'Heritage",
        "cuisine": "French",
        "location": "Mosman",
        "rating": 13
    },
    {
        "name": "arthur",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "Annata",
        "cuisine": "Bistro",
        "location": "St Leonards",
        "rating": 13
    },
    {
        "name": "The Apollo",
        "cuisine": "Greek",
        "location": "Potts Point",
        "rating": 13
    },
    {
        "name": "Infinity at Sydney Tower",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Bastardo",
        "cuisine": "Italian",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "Rockpool Bar & Grill Sydney",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Fior",
        "cuisine": "Modern Australian",
        "location": "Gymea",
        "rating": 13
    },
    {
        "name": "Bar Copains",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "Ennui",
        "cuisine": "Modern Australian",
        "location": "Haymarket",
        "rating": 13
    },
    {
        "name": "Restaurant Hubert",
        "cuisine": "French",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Besuto",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Figo Restaurant & Bar",
        "cuisine": "Italian",
        "location": "Rushcutters Bay",
        "rating": 13
    },
    {
        "name": "Porteno",
        "cuisine": "Tapas",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "King Clarence",
        "cuisine": "Asian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Icebergs Dining Room & Bar",
        "cuisine": "Italian",
        "location": "Bondi",
        "rating": 13
    },
    {
        "name": "Viand",
        "cuisine": "Thai",
        "location": "Woolloomooloo",
        "rating": 13
    },
    {
        "name": "The Botanica Vaucluse",
        "cuisine": "Modern Australian",
        "location": "Vaucluse",
        "rating": 13
    },
    {
        "name": "Quoi Dining",
        "cuisine": "French",
        "location": "Baulkham Hills",
        "rating": 13
    },
    {
        "name": "Berts",
        "cuisine": "Brasserie",
        "location": "Newport",
        "rating": 13
    },
    {
        "name": "Palazzo Salato",
        "cuisine": "Italian",
        "location": "East Sydney",
        "rating": 13
    },
    {
        "name": "Mr Wong",
        "cuisine": "Chinese",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Brasserie 1930",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Kiln",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Fontana",
        "cuisine": "Italian",
        "location": "Redfern",
        "rating": 13
    },
    {
        "name": "Otto Ristorante Sydney",
        "cuisine": "Italian",
        "location": "Woolloomooloo",
        "rating": 13
    },
    {
        "name": "The Charles",
        "cuisine": "French",
        "location": "East Sydney",
        "rating": 13
    },
    {
        "name": "CRICCA",
        "cuisine": "Italian",
        "location": "Windsor",
        "rating": 13
    },
    {
        "name": "Eleven Barrack",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Bar Infinita",
        "cuisine": "Italian",
        "location": "Gordon",
        "rating": 13
    },
    {
        "name": "Shell House The Dining Room & Terrace",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "a'Mare",
        "cuisine": "Italian",
        "location": "Sydney CBD",
        "rating": 13
    },
    {
        "name": "Kisuke",
        "cuisine": "Japanese",
        "location": "Potts Point",
        "rating": 13
    },
    {
        "name": "Kuon Omakase",
        "cuisine": "Raw Food",
        "location": "Haymarket",
        "rating": 13
    },
    {
        "name": "Toki Bistro & Bar",
        "cuisine": "Fusion",
        "location": "North Sydney",
        "rating": 13
    },
    {
        "name": "Fred's",
        "cuisine": "Modern Australian",
        "location": "Paddington",
        "rating": 13
    },
    {
        "name": "Kindred",
        "cuisine": "Italian",
        "location": "Darlington",
        "rating": 13
    },
    {
        "name": "Nomad Sydney",
        "cuisine": "Middle Eastern",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "R by Raita Noda.",
        "cuisine": "Japanese",
        "location": "Redfern",
        "rating": 13
    },
    {
        "name": "No 92 Wine Bar and Restaurant",
        "cuisine": "Mexican",
        "location": "Glebe",
        "rating": 13
    },
    {
        "name": "The Dining Room by James Viles",
        "cuisine": "Modern Australian",
        "location": "The Rocks",
        "rating": 13
    },
    {
        "name": "Omakase by Prefecture 48",
        "cuisine": "Modern Australian",
        "location": "East Sydney",
        "rating": 13
    },
    {
        "name": "Sydney Common",
        "cuisine": "Modern Australian",
        "location": "East Sydney",
        "rating": 13
    },
    {
        "name": "Ursula's Paddington",
        "cuisine": "Modern Australian",
        "location": "Paddington",
        "rating": 13
    },
    {
        "name": "Firepop",
        "cuisine": "Modern Australian",
        "location": "Enmore",
        "rating": 13
    },
    {
        "name": "Coya Sydney",
        "cuisine": "Middle Eastern",
        "location": "St Leonards",
        "rating": 13
    },
    {
        "name": "Oribu",
        "cuisine": "Japanese",
        "location": "Parramatta",
        "rating": 13
    },
    {
        "name": "Henrys Neutral Bay",
        "cuisine": "Fusion",
        "location": "Neutral Bay",
        "rating": 13
    },
    {
        "name": "Armorica",
        "cuisine": "French",
        "location": "Surry Hills",
        "rating": 13
    },
    {
        "name": "Chez Beckett's",
        "cuisine": "French",
        "location": "Chippendale",
        "rating": 13
    },
    {
        "name": "Cafe Paci",
        "cuisine": "Modern Australian",
        "location": "Newtown",
        "rating": 13
    },
    {
        "name": "Bistro George",
        "cuisine": "Bistro",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Jonah's",
        "cuisine": "European",
        "location": "Whale Beach",
        "rating": 12
    },
    {
        "name": "Mode Kitchen & Bar",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Urban Tadka",
        "cuisine": "Indian",
        "location": "Terrey Hills",
        "rating": 12
    },
    {
        "name": "Takam",
        "cuisine": "Filipino",
        "location": "Darlinghurst",
        "rating": 12
    },
    {
        "name": "Newmarket Room",
        "cuisine": "Modern Australian",
        "location": "Warwick Farm",
        "rating": 12
    },
    {
        "name": "Sella Vinoteca",
        "cuisine": "Italian",
        "location": "Randwick",
        "rating": 12
    },
    {
        "name": "Table Manners",
        "cuisine": "European",
        "location": "Bronte",
        "rating": 12
    },
    {
        "name": "Woodcut",
        "cuisine": "Modern Australian",
        "location": "Barangaroo",
        "rating": 12
    },
    {
        "name": "Abhi's",
        "cuisine": "Indian",
        "location": "North Strathfield",
        "rating": 12
    },
    {
        "name": "Sala",
        "cuisine": "Italian",
        "location": "Pyrmont",
        "rating": 12
    },
    {
        "name": "Loulou Bistro",
        "cuisine": "French",
        "location": "Milsons Point",
        "rating": 12
    },
    {
        "name": "Toei",
        "cuisine": "Asian",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Poetica Bar & Grill",
        "cuisine": "Modern Australian",
        "location": "North Sydney",
        "rating": 12
    },
    {
        "name": "Sails on Lavender Bay",
        "cuisine": "Modern Australian",
        "location": "McMahons Point",
        "rating": 12
    },
    {
        "name": "Clarence and V",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Osteria Coogee",
        "cuisine": "Italian",
        "location": "Coogee",
        "rating": 12
    },
    {
        "name": "Sinclair's",
        "cuisine": "Modern Australian",
        "location": "Penrith",
        "rating": 12
    },
    {
        "name": "RAFI",
        "cuisine": "Modern Australian",
        "location": "North Sydney",
        "rating": 12
    },
    {
        "name": "PELLEGRINO 2000",
        "cuisine": "Italian",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Seven Spices",
        "cuisine": "Indian",
        "location": "Lane Cove",
        "rating": 12
    },
    {
        "name": "The Dry Dock Public House and Dining Room",
        "cuisine": "European",
        "location": "Balmain",
        "rating": 12
    },
    {
        "name": "Maydanoz",
        "cuisine": "Turkish",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Epula",
        "cuisine": "European",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Vineria Luisa",
        "cuisine": "Italian",
        "location": "Enmore",
        "rating": 12
    },
    {
        "name": "Kazan Dining",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Cho Cho San",
        "cuisine": "Japanese",
        "location": "Potts Point",
        "rating": 12
    },
    {
        "name": "Cibaria Manly",
        "cuisine": "Italian",
        "location": "Manly",
        "rating": 12
    },
    {
        "name": "Bistro Moncur Woollahra",
        "cuisine": "French",
        "location": "Woollahra",
        "rating": 12
    },
    {
        "name": "Maiz Mexican Food",
        "cuisine": "Mexican",
        "location": "Newtown",
        "rating": 12
    },
    {
        "name": "Silvester's Restaurant & Lounge",
        "cuisine": "Modern Australian",
        "location": "Circular Quay",
        "rating": 12
    },
    {
        "name": "Poly",
        "cuisine": "International",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Hustlers. Syd",
        "cuisine": "Asian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Attenzione Food & Wine",
        "cuisine": "Italian",
        "location": "Redfern",
        "rating": 12
    },
    {
        "name": "Ho Jiak Townhall",
        "cuisine": "Asian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Entrata",
        "cuisine": "Italian",
        "location": "Glenhaven",
        "rating": 12
    },
    {
        "name": "Wagyuto",
        "cuisine": "Japanese",
        "location": "Clovelly",
        "rating": 12
    },
    {
        "name": "Public Dining Room",
        "cuisine": "Modern Australian",
        "location": "Balmoral Beach",
        "rating": 12
    },
    {
        "name": "Esteban",
        "cuisine": "Mexican",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Ito Restaurant",
        "cuisine": "Japanese",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Mister Grotto",
        "cuisine": "Seafood",
        "location": "Newtown",
        "rating": 12
    },
    {
        "name": "20 Chapel",
        "cuisine": "Steak",
        "location": "Marrickville",
        "rating": 12
    },
    {
        "name": "Lilymu",
        "cuisine": "Asian",
        "location": "Parramatta",
        "rating": 12
    },
    {
        "name": "Ibushi Robata Grill",
        "cuisine": "Japanese",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Bar Lettera",
        "cuisine": "Italian",
        "location": "North Sydney",
        "rating": 12
    },
    {
        "name": "Antica Dining",
        "cuisine": "Italian",
        "location": "North Sydney",
        "rating": 12
    },
    {
        "name": "Restaurant Leo",
        "cuisine": "Italian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "S'more",
        "cuisine": "French",
        "location": "Castlecrag",
        "rating": 12
    },
    {
        "name": "The Restaurant Pendolino",
        "cuisine": "Italian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Osteria Mucca",
        "cuisine": "Italian",
        "location": "Newtown",
        "rating": 12
    },
    {
        "name": "Porkfat Restaurant Sydney",
        "cuisine": "Thai",
        "location": "Haymarket",
        "rating": 12
    },
    {
        "name": "Bessie's & Alma's",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Shaffa",
        "cuisine": "Middle Eastern",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "Cottage Point Inn",
        "cuisine": "Modern Australian",
        "location": "Cottage Point",
        "rating": 12
    },
    {
        "name": "The Grill at The International",
        "cuisine": "Modern Australian",
        "location": "East Sydney",
        "rating": 12
    },
    {
        "name": "Tanuki Restaurant Sydney",
        "cuisine": "Japanese",
        "location": "Double Bay",
        "rating": 12
    },
    {
        "name": "Gran Torino",
        "cuisine": "Italian",
        "location": "Double Bay",
        "rating": 12
    },
    {
        "name": "Bistro Bondi",
        "cuisine": "European",
        "location": "Bondi Beach",
        "rating": 12
    },
    {
        "name": "Bistro Rex",
        "cuisine": "French",
        "location": "Potts Point",
        "rating": 12
    },
    {
        "name": "Midden by Mark Olive",
        "cuisine": "Modern Australian",
        "location": "Bennelong Point",
        "rating": 12
    },
    {
        "name": "Jane",
        "cuisine": "Modern Australian",
        "location": "Surry Hills",
        "rating": 12
    },
    {
        "name": "BTWN",
        "cuisine": "Modern Australian",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Sokyo",
        "cuisine": "Japanese",
        "location": "Pyrmont",
        "rating": 12
    },
    {
        "name": "Spice Temple Sydney",
        "cuisine": "Chinese",
        "location": "Sydney CBD",
        "rating": 12
    },
    {
        "name": "Amuro",
        "cuisine": "Japanese",
        "location": "Darlinghurst",
        "rating": 12
    },
    {
        "name": "ANTE",
        "cuisine": "Modern Australian",
        "location": "Newtown",
        "rating": 12
    },
    {
        "name": "Osteria di Russo & Russo",
        "cuisine": "Italian",
        "location": "Enmore",
        "rating": 12
    }
]


# Remove repeated cuisines
cuisines = []

for restaurant in restaurants:
    if restaurant["cuisine"] not in cuisines:
        cuisines.append(restaurant["cuisine"])

cuisines.sort()


# Ask the user to choose a cuisine
cuisine = ""

while cuisine != "quit":

    # Show available cuisines
    print()
    print("Available cuisines:")

    for food in cuisines:
        print(food)

    print()
    cuisine = input("What type of food would you like? (Type 'quit' to exit):").lower()
    print()


    if cuisine != "quit":
        


        # Find locations with the chosen cuisine
        locations = []

        for restaurant in restaurants:
            if restaurant["cuisine"].lower() == cuisine:
                if restaurant["location"] not in locations:
                    locations.append(restaurant["location"])

        locations.sort()



        # Check the cuisine
        if not locations:
            print()
            print("Sorry, we couldn't find the cuisine. Please try again.")
            print()
            continue

                    

        # Show available locations
        print()
        print("Available locations:")

        for location in locations:
            print(location)
            

        # Ask the user to choose a location
        location = ""
        valid_locations = []


        for place in locations:
            valid_locations.append(place.lower())


        while location not in valid_locations and location != "quit":
            print()
            location = input("Which location would you like? (Type 'quit' to exit): ").lower()
            print()
            

            if location not in valid_locations and location != "quit":
                print()
                print("Sorry, we couldn't find that location. Please try again.")
                print()



        # Exit if the user enters quit
        if location == "quit":
            cuisine = "quit"
            break
        


        # Find ratings with the chosen cuisine and location
        ratings = []
        
        for restaurant in restaurants:
            if restaurant["cuisine"].lower() == cuisine and restaurant["location"].lower() == location:
                if restaurant["rating"] not in ratings:
                    ratings.append(restaurant["rating"])
                    


        
        # Ask the user to choose a minimum rating
        if len(ratings) == 1:
            minimum_rating = ratings[0]
        else:
            
            # Explain Chef Hat ratings
            print()
            print("Chef Hat ratings are based on food quality (out of 20).")
            print("19-20: Superlative Food & Wine")
            print("17-18: Exceptional Quality of Cuisine")
            print("15-16: Food Quite Out of the Ordinary")
            print("13-14: A Good Restaurant in its category")
            print("12: Commended")
            print()

            # Show available ratings
            print("Available Chef Hat ratings:")

            for rating in ratings:
                print(rating)
            print()
            
            minimum_rating = int(input("What is the minimum Chef Hat rating you would accept? (Restaurants with this rating or higher will be shown): "))
        


        # Find restaurants that meet the minimum rating
        matched_restaurants = []

        while len(matched_restaurants) == 0:

            matched_restaurants = []
            
            for restaurant in restaurants:
                if restaurant["cuisine"].lower() == cuisine and restaurant["location"].lower() == location:
                   if restaurant["rating"] >= minimum_rating:
                       matched_restaurants.append(restaurant)


            # If no restaurants match, ask for a lower rating
            if len(matched_restaurants) == 0:
                print()
                print("Sorry, no restaurants meet your minimum rating. Please try a lower rating.")
                print()

                minimum_rating = int(input("What is your new minimum Chef Hat rating?"))
                    



        # Randomly recommend a restaurant
        remaining_restaurants = matched_restaurants.copy()
        choice = "1"

        while choice == "1":
            
            selected_restaurant = random.choice(remaining_restaurants)
        
            print()
            print("DineDecide recommends:")
            print(selected_restaurant["name"], selected_restaurant["rating"])
            print()

            
            # Avoid recommending the same restaurant again
            remaining_restaurants.remove(selected_restaurant)
            

            # Check if all restaurants have been recommended
            if len(remaining_restaurants) == 0:
                print("You've seen all available restaurants!")
                print()

                print("What would you like to do next?")
                print("2. Choose another cuisine")
                print("3. Quit")
                

                choice = input("Enter your choice: ")
                

                # Check the user's input
                while choice != "2" and choice != "3":
                    print("Please enter 2 or 3.")
                    choice = input("Enter your choice: ")
                break
            
            
            # Show options if there are restaurants left
            
            print("What would you like to do next?")
            print("1. Recommend another restaurant")
            print("2. Choose another cuisine")
            print("3. Quit")

            choice = input("Enter your choice: ")
            

            # Check the user's input
            while choice != "1" and choice != "2" and choice != "3":
                print("Please enter 1, 2 or 3.")
                choice = input("Enter your choice: ")
                

        # Check if the user wants to choose another cuisine or quit
        if choice == "2":
            print()
            continue
        elif choice == "3":
            cuisine = "quit"
        print()


print("Thanks for using DineDecide!")
        








         
   
