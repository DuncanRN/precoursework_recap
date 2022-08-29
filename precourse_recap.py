city_1 = "glasgow"
city_2 = "edinburgh"
city_3 = "dundee"
country_1 = "scotland"

city_1 = city_1.capitalize()
city_2 = city_2.capitalize()
city_3 = city_3.capitalize()
country_1 = country_1.capitalize()


print(city_1 + ", " + city_2 + ", " + city_3 + ", " + "are all in " + country_1 + ".")


scottish_pop = 5454000
united_kingdom_pop = 67220000

print("Scotland's population - " + str(scottish_pop))
print("The United Kingdom's population - " + str(united_kingdom_pop))
percentage_of_pop = round(scottish_pop / united_kingdom_pop, 2 ) * 100

percentage_of_pop_string = str(percentage_of_pop)

print("so Scotland makes up " + percentage_of_pop_string + "% of the UK's population")