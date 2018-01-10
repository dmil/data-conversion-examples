# read superheros.json
import json
from pprint import pprint

with open('superhero.json') as f:
    data = json.load(f)

# Create a blank list of powers
powers = []


members = data['members']
# Loop over members
for member in members:
	# for each member , loop over powers
	member_powers = member['powers']
	for power in member_powers:
		# add that to our list of powers
		powers.append(power)



# get only unique elements
unique_powers = list(set(powers))

# print those unique elements
pprint(unique_powers)