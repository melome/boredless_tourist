#THE BOREDLESS TOURIST

destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveller = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
print(destinations)

def get_destination_index(traveler_destination):
    for index in range(len(destinations)):
        if traveler_destination == destinations[index]:
            destination_index = index
    return destination_index

print(get_destination_index("Paris, France"))

def get_traveler_location(traveler):
    traveler_destination = destinations[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveller)
print(test_destination_index)

