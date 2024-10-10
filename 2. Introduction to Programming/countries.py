countries = ['France', 'Brazil', 'Australia', 'Portugal', 'Chad', 'Spain', 'China', 'Russia', 'Austria', 'India']
print(countries) # printing out a list

# creating empty list
countries = []

# appending to list, empty or not
countries.append('France')
countries.append('Brazil')
countries.append('Australia')
countries.append('Portugal')
countries.append('Chad')
countries.append('Spain')
countries.append('China')
countries.append('Russia')
countries.append('Austria')
countries.append('India')
print(countries)

# removing items from the list by value
countries.remove('Russia')
print(countries) # print countries without Russia

# removing items from the list by index position
countries.pop(0) # pop France
print(countries) # removed Russia, popped France :3

# returns index position of the element
print(countries.index('China'))

# returns the value at the given at the given index position
print(countries[2])

# returns the length of the list
print(len(countries))

# reverse the elements of the list
countries.reverse()
print(countries)

# sort the list alphabetically
countries.sort()
print(countries)


countries_1 = ['Spain', 'China', 'Russia', 'Austria', 'India']
countries_2 = ['France', 'Brazil', 'Australia', 'Portugal', 'Chad']
merged_countries = countries_1 + countries_2 * 10**8

print(merged_countries)