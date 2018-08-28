# Runtime:
# n is the number of lines
# m is the number of unique (date, hostname) pair
# O(n) + O(m lg(m))
# O(n) from iterating each line, and count the pair (date, hostname) in a hash map
# O(m lg(m)) for sorting the (date, hostname) ordered by (date, count)
# printing with groupby iterator is linear
from collections import defaultdict
from datetime import datetime
from itertools import groupby
from sys import argv

count_map = defaultdict(int)
with open(argv[1]) as f:
    for line in f:
        timestamp, url = line.rstrip().split('|')
        utc_date = datetime.utcfromtimestamp(int(timestamp)).strftime('%m/%d/%Y')
        count_map[(utc_date, url)] += 1
sorted_keys = sorted(count_map.keys(), key=lambda i: (i[0], -count_map[i]))
for group_date, utc_date_urls in groupby(sorted_keys, key=lambda i: i[0]):
    print(group_date, 'GMT')
    for utc_date_url in utc_date_urls:
        url = utc_date_url[1]
        print(url, count_map[utc_date_url])
