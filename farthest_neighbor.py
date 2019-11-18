
def farthest_neighbor_sort(entries, lookback_size=150):

	# "lookback_size" is the number of most recently added entries
	# to try to avoid.
	# So while evaluating candidates to add to our newly sorted list,
	# we will compare the "lookback_size"-most recently added entries
	# and select a candidate that is maximally far away. 

	# start with any item in the original list.
	sorted_entries = [entries.pop()]

	def farthest_key(entry):

		x0 = entry[0]
		y0 = entry[1]

		# start with a very large distance.
		distance = 100000

		for other_entry in sorted_entries[-lookback_size:]:
			
			x1 = other_entry[0]
			y1 = other_entry[1]

			diffx = x1-x0
			diffy = y1-y0

			# only the squared distance matters during comparisons
			new_distance = diffx*diffx+diffy*diffy 
			distance = min(distance, new_distance)

		return distance

	count = 1

	while entries:

		entries = sorted(entries, key=farthest_key)

		sorted_entries.append(entries.pop())

		count += 1
		print('completed: ' + str(count))

	return sorted_entries


if __name__ == '__main__':

	import random
	import csv

	entries = [[random.random(),random.random()] for i in range(100)]
	sorted_entries = farthest_neighbor_sort(entries, lookback_size=150)

	print('saving random_stuff.csv')
	with open('random_stuff.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',')

		for entry in sorted_entries:
			writer.writerow(entry)
