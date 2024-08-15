# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# # Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin"], "total_visits": 1},
#     'Belgium': {'cities_visited': ['Brussels', 'Bruges'], 'total_visits': 12}
# }

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin"],
        "total_visits": 1,
    },
    {
        "country": "Belgium",
        "cities_visited": ["Brussels", "Bruges"],
        "total_visits": 12,
    },
]

# Coding Challenge: Dictionary in List


def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["cities"] = cities
    new_country["total_visits"] = visits
    travel_log.append(new_country)


# Don't change the code below 👇
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
