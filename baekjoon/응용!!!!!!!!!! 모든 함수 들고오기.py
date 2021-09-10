from itertools import combinations,chain
def get_all_subset(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

iterable=[1,0]
print(list(get_all_subset(iterable)))