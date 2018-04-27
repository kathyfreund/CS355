import inspect
import math

debugging = True
def debug(*s): 
	if debugging: 
		print(*s)


#*****************PROBLEM 1 - DICTIONARIES**************************
#create new dictionary(T) for totals
#go through days of week
	#go through classes studied
		#if lecture already in T
			#add value to existing element to T
		#else
			#make new class and add to T
			#assign value to new element
	#print out L
def addDict(d):
	nd = {}
	for day, classes in d.items():
		for lecture, hours in classes.items():
			if lecture in nd.keys():
				nd[lecture] += hours
			else:
				nd[lecture] = hours
	return nd

def testaddDict():
		d = {'Mon':{'355':2,'451':1,'360':2},'Tue':{'451':2,'360':3},'Thu':{'355':3,'451':2,'360':3}, 'Fri':{'355':2},'Sun':{'355':1,'451':3,'360':1}} 
		trued = {'355': 8, '451': 8, '360': 9}
		testd = addDict(d)
		if testd == trued:
			return True
		else:
			return False
			

#same as addDict, but now with an extra loop to go through L			
def addDictN(L):
	nd = {}	
	for n in L:
		for day, classes in n.items():
			for lecture, hours in classes.items():
				if lecture in nd.keys():
					nd[lecture] += hours
				else:
					nd[lecture] = hours
	return nd
		
def testaddDictN():
		d = [{'Mon':{'355':2,'360':2},'Tue':{'451':2,'360':3},'Thu':{'360':3},'Fri':{'355':2}, 'Sun':{'355':1}},{'Tue':{'360':2},'Wed':{'355':2},'Fri':{'360':3, '355':1}},{'Mon':{'360':5},'Wed':{'451':4},'Thu':{'355':3},'Fri':{'360':6},'Sun':{'355':5}}]
		trued = {'355': 16, '360': 24, '451': 6}
		testd = addDictN(d)
		if testd == trued:
			return True
		else:
			return False
		
		
		
		
		

		
#*****************PROBLEM 2 - lIST COMPREHENSION**************************		
#same logic as addDict, but convert over to tuples + sort
		
def charCount(s):
	d = {}
	for i in s:
		if i in d.keys():
			d[i] += 1
		elif i == " ":
			continue
		else:
			d[i] = 1
	L = d.items()
	return sorted(L,key=lambda x:(x[1],x[0]))
		
def testcharCount():
	s = 'Cpts355 --- Assign1'
	tests = charCount(s)
	trues = [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]
	if tests == trues:
		return True
	else:
		return False
		

def charCount2(s):
	d = {}
	for i in s:
		if i in d.keys():
			continue
		elif i == " ":
			continue
		else:
			d[i] = s.count(i)
	L = d.items()
	return sorted(L,key=lambda x:(x[1],x[0]))

	
def testcharCount2():
	s = 'Cpts355 --- Assign1'
	tests = charCount2(s)
	trues = [('1', 1), ('3', 1), ('A', 1), ('C', 1), ('g', 1), ('i', 1), ('n', 1), ('p', 1), ('t', 1), ('5', 2), ('-', 3), ('s', 3)]
	if tests == trues:
		return True
	else:
		return False
		
		
		
		
		
		
#*****************PROBLEM 3 - lIST + DICTIONARY**************************		
#reverse lists, return first instance.
#check second element in tuple. if not found, return first element (recursion)	
		
def lookupVal(L, k):
	for i in reversed(L):
		for x,y in i.items():
			if x == k:
				return i[x]
			else:
				continue
	return None
		
def testlookupVal():
	L1 = [{"x":1, "y":True, "z":"found"}, {"x":2}, {"y":False}]
	tests = lookupVal(L1, "t")
	trues = None
	if tests == trues:
		return True
	else:
		return False
		
		
def lookupVal2(tL, k):
	def lookupHelper(i, tL, k):
		if k in tL[i][1]:
			return tL[i][1][k]
		elif i == tL[i][0]:
			return None
		else:
			return lookupHelper(tL[i][0], tL, k)
	i = len(tL) - 1
	return lookupHelper(i, tL, k)
		
def testlookupVal2():
	L2 = [(0,{"x":0,"y":True,"z":"zero"}),(0,{"x":1}),(1,{"y":False}),(1,{"x":3, "z":"three"}),(2,{})]
	tests = lookupVal2(L2, "t")
	trues = None
	if tests == trues:
		return True
	else:
		return False		
		
		
		
		

#*****************PROBLEM 4 - HIGHER ORDER FUNCTIONS**************************		
#https://stackoverflow.com/questions/2525845/proper-way-in-python-to-raise-errors-while-setting-variables	
		
def funRun(d, name, args):
	if len(args) == len(inspect.getfullargspec(d[name]).args):
		return d[name](*args)
	else:
		raise TypeError("ERROR: Number of inputs do not match required number of arguments.")
		
		
def testfunRun():
	d = {"add": lambda x,y: (x+y), "concat3": lambda a,b,c:(a+","+b+","+c),"mod2": lambda n: (n % 2)}
	tests = funRun(d, "mod2", [40])
	trues = 0
	if tests == trues:
		return True
	else:
		return False		
		
		
		
		
		
		
#*****************PROBLEM 5 - RECUSION**************************		
#let recursion do the dirty work
		
def numPaths(m,n):
	if(m == 1 or n == 1):
		return 1
	else:
		return numPaths(m-1, n) + numPaths(m, n-1)
		
def testnumPaths():
	tests = numPaths(3,3)
	trues = 6
	if tests == trues:
		return True
	else:
		return False		
		
		
		
		
		
		
		
		
#*****************PROBLEM 6 - ITERATORS**************************		
#https://stackoverflow.com/questions/30254640/calculating-the-square-numbers-within-a-range-python
				
class iterSquares(object):
	def __init__(self):
		self.current = 1
	def __next__(self):
		result = self.current
		self.current = (int(math.sqrt(result)) + 1) ** 2
		return result
	def __iter__(self):
		return self
		
		
def numbersToSum(iNumbers, sum):
	L = []
	count = 0
	peek = iterSquares()
	peek.__next__()
	for n in iNumbers:
		if (count + n > sum):
			break
		elif (count + n < sum):
			L.append(n)
			count += n
			if (count + peek.__next__() >= sum):
				break
	return L
		
	
def testnumbersToSum():
	s = iterSquares()
	tests = numbersToSum(s,55)
	trues = [1,4,9,16]
	test2 = numbersToSum(s,100)
	true2 = [25, 36]
	#print(tests)
	#print(test2)
	if tests == trues:
		return True
	else:
		return False








		
		
		
		
		
#*****************PROBLEM 7 - STREAMS**************************		
#stream class given in class
class Stream(object):
	def __init__(self, first, compute_rest, empty= False):
		self.first = first
		self._compute_rest = compute_rest
		self.empty = empty
		self._rest = None
		self._computed = False

	@property
	def rest(self):
		assert not self.empty, 'Empty streams have no rest.'
		if not self._computed:
			self._rest = self._compute_rest()
			self._computed = True
		return self._rest

		
def streamSquares(k):
	def compute_rest():
		return streamSquares((int(math.sqrt(k)) + 1) ** 2)
	return Stream(first = k, compute_rest = compute_rest)
		
def teststreamSquares():
	sqStream = streamSquares(25)
	myList = []
	while sqStream.first < 225:
		myList.append(sqStream.first)
		sqStream =sqStream.rest
	trues = [25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
	if myList == trues:
		return True
	else:
		return False
		
		
def evenStream(stream):
	def evenCheck(x):
		if ((x % 2) == 0):
			return True
		else:
			return False
	def compute_rest():
		return evenStream(stream.rest.rest)
	return Stream(stream.first if evenCheck(stream.first) else stream.rest.first, compute_rest)


def testevenStream():
	evenS = evenStream(streamSquares(9))
	myList = []
	while evenS.first < 225:
		myList.append(evenS.first)
		evenS =evenS.rest
	trues = [16, 36, 64, 100, 144, 196]
	if myList == trues:
		return True
	else:
		return False
	
		
if __name__ == '__main__':
	passedMsg = "%s passed"
	failedMsg = "%s failed"
	if testaddDict():
		print(passedMsg % 'addDict')
	else:
		print(failedMsg % 'addDict')
		
	if testaddDictN():
		print(passedMsg % 'addDictN')
	else:
		print(failedMsg % 'addDictN')
		
	if testcharCount():
		print(passedMsg % 'charCount')
	else:
		print(failedMsg % 'charCount')
		
	if testcharCount2():
		print(passedMsg % 'charCount2')
	else:
		print(failedMsg % 'charCount2')
		
	if testlookupVal():
		print(passedMsg % 'lookupVal')
	else:
		print(failedMsg % 'lookupVal')
		
	if testlookupVal2():
		print(passedMsg % 'lookupVal2')
	else:
		print(failedMsg % 'lookupVal2')
		
	if testfunRun():
		print(passedMsg % 'funRun')
	else:
		print(failedMsg % 'funRun')
		
	if testnumPaths():
		print(passedMsg % 'numPaths')
	else:
		print(failedMsg % 'numPaths')
		
	if testnumbersToSum():
		print(passedMsg % 'numbersToSum')
	else:
		print(failedMsg % 'numbersToSum')
	
	if teststreamSquares():
		print(passedMsg % 'streamSquares')
	else:
		print(failedMsg % 'streamSquares')
		
	if testevenStream():
		print(passedMsg % 'evenStream')
	else:
		print(failedMsg % 'evenStream')