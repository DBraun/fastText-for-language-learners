import numpy as np
import csv
from farthest_neighbor import farthest_neighbor_sort

import umap

FASTTEXT_OUTPUT_FILE = 'output.txt'

# the result of the UMAP process, comma separated, two columns
EMBEDDING_FILE = 'embedding.csv'

# many lines of words. each line has no white space.
QUERIES_FILE = 'queries.txt'

UNSORTED_FILE = 'unsorted_queries.csv'
SORTED_FILE = 'sorted_queries.csv'

a = np.loadtxt(open(FASTTEXT_OUTPUT_FILE, encoding='utf-8'),usecols=[i for i in range(1,301)])
embedding = umap.UMAP(n_neighbors=10).fit_transform(a)

np.savetxt(EMBEDDING_FILE,embedding,delimiter=',',fmt='%f')

embedding = np.loadtxt(open(EMBEDDING_FILE, encoding='utf-8'),delimiter=',')

words = np.genfromtxt(open(QUERIES_FILE, encoding='utf-8'),dtype='str')

words = np.asmatrix(words).T

data = np.concatenate((embedding,words),axis=1)

# convert from numpy to python list
old_data = data.tolist()
# data = [['-1.2315','1.345','word'],['0.840','1.7325','another'],...]

# Cast the first and second columns to float numbers.
# Use the '*' trick in python to get any additional remaining columns.
unsorted = []
for row in old_data:
	unsorted.append([
		float(row[0]),
		float(row[1]),
		*row[2:]
		])

print('saving: '+UNSORTED_FILE)
with open(UNSORTED_FILE, 'w', newline='\n', encoding='utf-8') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')

	for entry in unsorted:
		writer.writerow(entry)

sorted_entries = farthest_neighbor_sort(unsorted, lookback_size=150)

print('saving: '+SORTED_FILE)
with open(SORTED_FILE, 'w', newline='\n', encoding='utf-8') as csvfile:
	writer = csv.writer(csvfile, delimiter=',')

	for entry in sorted_entries:
		writer.writerow(entry)
