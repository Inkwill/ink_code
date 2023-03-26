def scan(content):

	wordsDict = {'direction':'north south east west down up left right back',
				'verb':'go stop kill eat is',
				'stop':'the in of from at it to',
				'noun':'door bear princess cabinet girl i home school',
				}
	clist = content.split()
	result = []

	# check content in wordsDict, return a new tuple :(key,value)
	import math
	for c in clist:
		try:
			num = float(c)
			result.append(('number',str(c)))
		except ValueError:
			err = True
			for d in wordsDict:
				if c.lower() in wordsDict[d].split():
					err = False
					result.append((d,c))
			if err:
				result.append(('error',c))
	return result
