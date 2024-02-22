""" 
Make a dictionary called cities. Use the name of three cities as keys in your dictionary.
Create a dictionary of information about each city and include the country that the city
is in, its approximate population, and one fact about that city. The keys for the city's 
dictionary should be Country of Origin, Population, and Fact. Then by using the for loop,
print out each city from the cities dictionary and all the city's information. 
"""

cities = {"Denver": {"Country of Origin":"USA",
                     "Population":711463,
                     "Fact":"Home of the Broncos."},
          "Bratislava":{"Country of Origin":"Slovakia",
                        "Population":424428,
                        "Fact":"It is the capital city of Slovakia."},
          "Brussels": {"Country of Origin":"Belgium",
                       "Population":1209000,
                       "Fact":"Seat of the EU Parliament"}
          }

for city, information in cities.items():
	print(f"The name of the city is {city} and its information is this:")
	print(f"{information}")
	print()