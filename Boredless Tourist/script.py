destinations = ["Paris, France","Shanghai, China","Los Angeles, USA", "São Paulo, Brazil","Cairo, Egypt"]

test_traveller = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
	destination_index = destinations.index(destination)
  	return destination_index

## print(get_destination_index("Los Angeles, USA"))

def get_traveller_index(traveler):
	traveler_destination = traveler[1]
	traveler_destination_index = get_destination_index(traveler_destination)
	return traveler_destination_index

print(get_traveller_index(test_traveller))


## Wait for input allow read  ##
raw_input()
