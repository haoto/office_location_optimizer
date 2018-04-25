# -*- coding: utf8 -*-
import googlemaps
from datetime import datetime, timezone, timedelta
import numpy as np

google_maps_api_key = open('api_key', 'r').read().rstrip('\n')
origins = open('origins', 'r').read().splitlines()
destinations = open('destinations', 'r').read().splitlines()

arrival_time = datetime(2018, 4, 26, 8, 50, tzinfo=timezone(timedelta(0, 8*3600)))
batch_size = 10

gmaps = googlemaps.Client(key=google_maps_api_key)

dists = np.zeros((len(origins), len(destinations)))

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

batches = list(chunks(range(0, len(destinations)), batch_size))

for i_batch in range(0, len(batches)):
    i_dests = batches[i_batch]
    dests_batch = [destinations[i] for i in i_dests]

    distance_matrix_result = gmaps.distance_matrix(origins,
            dests_batch,
            arrival_time=arrival_time,
            mode='transit')
    
    for i_orig, r in enumerate(distance_matrix_result['rows']):
        for i_dest_batch, e in enumerate(r['elements']):
            i_dest = i_dests[i_dest_batch]
            dists[i_orig][i_dest] = e['duration']['value']

dists_max = [max(x) for x in zip(*dists)]
dists_mean = sum(dists) / len(origins)

# print('Max commute time per destination:', dists_max)
# print('Mean commute time per destination:', dists_mean)

i_sort_max = np.argsort(dists_max)
print('\nBest location by max commute time (seconds):')
for i in range(0, len(destinations)):
    print(i+1, dists_max[i_sort_max[i]], destinations[i_sort_max[i]])

i_sort_mean = np.argsort(dists_mean)
print('\nBest location by mean commute time (seconds):')
for i in range(0, len(destinations)):
    print(i+1, dists_mean[i_sort_mean[i]], destinations[i_sort_mean[i]])
