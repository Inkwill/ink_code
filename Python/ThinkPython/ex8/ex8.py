import pandas as pd

# ex8.2
def statistics_wordlen():
	'''read words that  less than 20 characters'''
	fin = open('words.txt')
	words = pd.Series(list(fin))
	len_words = words.apply(lambda x:len(x.strip()))
	result = pd.DataFrame({"count":len_words.value_counts(sort=False),
							"frequency":len_words.value_counts(True)
															})
	print(result)
		

statistics_wordlen()

# ex8.3
