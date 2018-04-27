#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = []

def opPop():	if(len(opstack) > 0):		return opstack.pop()	else:		print("[!] ERROR - List is empty.")def opPush(value):	opstack.append(value)
#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations 
dictstack = []
 
def dictPop():
	if(len(dictstack) > 0):		return dictstack.pop()	else:		print("[!] ERROR - List is empty.")

def dictPush(d):
	dictstack.append(d)


def define(name, value):
	if not dictstack:
		d = {}
		d[name] = value
		dictstack.append((0,d))
	else:
		(dictstack[-1][1])[name] = value
 

def lookup(name, scope):
    #print("looking for ...", name)
    name = '/' + name
    if scope == 'dynamic': #search through first dict
        for t in reversed(dictstack):
            #print(d)
            i, d = t
            if name in d:
                #print("PASS")
                return (i, d[name])
        else:
            return None
    else: #search through all dicts
        #print("DICTSTACK ->  ", dictstack)
        #print()
        #if name in dictstack[-1][1]:
            #return (dictstack[-1][0], dictstack[-1][1][name])
        #else:
        i = len(dictstack) - 1
        d = list(dictstack)
        #print()		
        return lookupHelper(d, name, i)

		
def lookupHelper(d, c, i):
    #print(dictstack[i][1])
    if c in dictstack[i][1]:
        #print(i, dictstack[i][1][c])
        #print()
        return (i, dictstack[i][1][c])
    elif i == dictstack[i][0]:
        return None
    else:
        next, _ = dictstack[i]
        _ = d.pop(i)
        return lookupHelper(d, c, next)
	
def getlink(i, tok):
	if(tok in dictstack[i]) or (i is 0):
		return i
	return getlink(dictstack[i][0], tok)

#--------------------------- 10% -------------------------------------
# Arithmetic operations: define all the arithmetic operators
def add():
	op1 = opPop()
	op2 = opPop()
	opPush(op1 + op2)
	
def sub():
	op1 = opPop()
	op2 = opPop()
	opPush(op2 - op1)
	
def mul():
	#print(opstack)
	op1 = opPop()
	op2 = opPop()
	opPush(op1 * op2)

def div():
	op1 = opPop()
	op2 = opPop()
	opPush(op2 / op1)

def mod():
	op1 = opPop()
	op2 = opPop()
	opPush(op2 % op1)

#--------------------------- 15% -------------------------------------
# Array operators: define the array operators -- length, get
def length():
	op1 = opPop()
	if type(op1) == list:
		opPush(len(op1))
	else:
		print("[!] ERROR - Input is not an array.")
		
def get():
    try: #http://www.pythonforbeginners.com/error-handling/python-try-and-except
        i = int(opPop())
        arr = opPop()
        assert type(arr) == list
        opPush(arr[i])
    except ValueError:
        print("[!] ERROR - Not an integer.")
    except AssertionError:
        print("[!] ERROR - Not an list.")
    except IndexError:
        print("[!] ERROR - Index bigger than list.")
		
		
def psFor():
	arr = opPop()
	f = opPop()
	i = opPop()
	x = opPop()
	#print(x)
	#print(f)
	#print(i)
	#print(arr)
	if isinstance(arr, list):
		if i > 0:
			for z in range(x, f+1, i):
				opPush(x)
				interpretSPS(arr)
		elif i < 0:
			#print("BREAKPOINT")
			for z in range(x, f, i):
				#print(x)
				opPush(z)
				interpretSPS(arr)
	else:
		print("[!] ERROR - Not an array.")
		
#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators -- dup, exch, pop, roll, copy, clear, stack
def dup():
	if opstack:
		opPush(opstack[-1])
	else:
		print("[!] ERROR - Stack is empty.")	
	
def exch():
	if len(opstack) >= 2:
		top = opPop()
		next = opPop()
		opPush(top)
		opPush(next)
	else:
		print("[!] ERROR - Insufficient inputs.")
	
def pop():
	if opstack:
		opPop()
	else:
		print("[!] ERROR - Stack is empty.")
	
def roll():
	if len(opstack) >= 2:
		numOfRolls = opstack[-1]
		n = opstack[-2]
		if isinstance(n, int) and isinstance(numOfRolls, int):
			if n > len(opstack):
				print("[!] ERROR - Insufficient inputs.")
			elif n < 0:
				print("[!] ERROR - Negative inputs.")
			elif numOfRolls >= 0:
				numOfRolls = opPop()
				n = opPop()
				if(n != 0 and n != 1):	
					for count in range(numOfRolls):
						val = opPop()
						opstack[-1*n+1:-1-n+1] = opstack[-1*n+1:-1-n+1] +[val]
			elif numOfRolls < 0:
				numOfRolls = opPop()
				n = opPop()
				if (n != 0 and n != 1):
					n = (-n)
					numOfRolls = (-numOfRolls)
					for count in range(numOfRolls):
						val = opstack.pop(n)
						opstack.append(val)
		else:
			print("[!] ERROR - Incorrect input type.")
	else:
		print("[!] ERROR - Insufficient inputs.")
	

def copy():
	items = int(opPop())
	if items > len(opstack) or items < 0:
		print("[!] ERROR - Exceeding inputs.")
	else:
		opstack.extend(opstack[len(opstack) - items:])
		
def clear():
	opstack.clear()
	dictstack.clear()
	
def stack():
    #print(dictstack)
    #print(opstack)
    print("==============")
    for x in reversed(opstack):
        print(x)
    print("==============")
    for i, t in reversed(list(enumerate(dictstack))): #https://stackoverflow.com/questions/36244380/enumerate-for-dictionary-in-python
        sl, d = t
        print('----',i ,'----',sl,'----')
        if d:
            for key in d:
                print(key, d[key])
    print("==============")	
	
#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDef

def psDef():
	if(len(opstack)) > 1:
		op1 = opPop()
		op2 = opPop()
		if isinstance(op1, int) or isinstance(op1, float) or isinstance(op1, list):
			define(op2, op1)
		elif isinstance(op2, int) or isinstance(op2, float):
			define(op1, op2)
		else:
			print("[!] ERROR - No variable.")
	else:
		print("[!] ERROR - Insufficient inputs.")
		
#----------------------------- PART 2 START ----------------------------
import re

def tokenize(s):
	retValue = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
	return retValue
	
def groupMatching(it):
	res = []
	for c in it:
		if c == '}':
			return res
		elif c == '{':
			res.append(groupMatching(it))
		else:
			res.append(c)
	return False
	
	
#def group(s):
#	if(s[0] == '(':
#		return groupMatching(iter(s[1:]))
#	else:
#		return False
		
#group(('(()(()))')


def parse(tokens):
	listtok = []
	it = iter(tokens)
	for c in it:
		#print(c)
		if isinstance(c, list):
			listtok.append(parse(c))
		elif c == '}':
			return False
		elif c == '{':
			g = groupMatching(it)
			listtok.append(parse(g))
		elif c.isdigit():
			listtok.append(int(c))
			#print("IS A INT")
		elif c.startswith('-'):
			listtok.append(int(c))
			#print("IS A NEG INT")
		else:
			if c.startswith('['): #regex doesn't convert lists
				foo = c[1:-1]
				temp = [int(k) for k in c[1:-1].split(' ')]
				listtok.append(temp)
				#print("IS A LIST")
			else:
				#print("IS A STRING")
				listtok.append(c)
	return listtok


def interpretSPS(code, scope):
	mop = {"dup": dup, "exch": exch, "pop": pop, "roll": roll, "copy": copy, "clear": clear, "stack": stack, "add": add, "sub": sub, "mul": mul, "div": div, "mod": mod, "def": psDef, "length": length, "get": get, "for": psFor}
	for c in code:
		#print(c)
		if isinstance(c, int):
			opPush(c)
		elif isinstance(c, str):
			if c.startswith('/'): #declare
				opPush(c)
			elif c in mop.keys(): #call
				#print("calling..", mop[c])
				mop[c]()
			else: #function call
				i, look = lookup(c, scope)
				#print("BREAKPOINT")
				if look != None:
					if isinstance(look, list):
						dictPush((i, {}))
						interpretSPS(look, scope)
						dictPop()
					else:
						opPush(look)
				else:
					print("[!] ERROR - Unknown item 1.")
					#print(c)
		elif isinstance(c, list):
			opPush(c)
		else:
			print("[!] ERROR - Unknown item 2.")
			#print(c)
		#print(dictstack)

def interpreter(s, scope):
    print()
    print("*****", scope, "*****")
    interpretSPS(parse(tokenize(s)), scope)
    print()	

	

    

#------- Part 2 TEST CASES--------------

		
def intertest1():
    print("~~~~~~~~~~~~~~~~~~~~~~TEST 1~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    clear()
    t = [7]
    interpreter(
"""
/x 4 def
/g { x stack } def
/f { /x 7 def g } def
f
""", 'dynamic')
    if list(reversed(opstack)) != t:
        return False
    

    clear()	
    t = [4]
    interpreter(
"""
/x 4 def
/g { x stack } def
/f { /x 7 def g } def
f
""", 'static')
    if list(reversed(opstack)) != t:
        return False
    else:
        return True

		
		
def intertest2():
    print("~~~~~~~~~~~~~~~~~~~~~~TEST 2~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    clear()
    t = [1, 100, 1, 50, 100]
    interpreter(
"""
/m 50 def
/n 100 def
/egg1 {/m 25 def n} def
/chic {
 /n 1 def
 /egg2 { n } def
 m n
 egg1
 egg2
 stack } def
n
chic
""", 'static')
    #print(reversed(opstack))
    if list(reversed(opstack)) != t:
        return False
	
    clear()
    #print("BREAKPOINT")
    #print(dictstack)
    t = [1, 1, 1, 50, 100]
    interpreter(
"""
/m 50 def
/n 100 def
/egg1 {/m 25 def n} def
/chic {
 /n 1 def
 /egg2 { n } def
 m n
 egg1
 egg2
 stack } def
n
chic
""", 'dynamic')
    if list(reversed(opstack)) != t:
        return False
    else:
        return True

		
		
def intertest3():
    print("~~~~~~~~~~~~~~~~~~~~~~TEST 3~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    clear()
    t = [10]
    interpreter(
"""
/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C stack} def
B
""", 'static')
    if list(reversed(opstack)) != t:
        return False
	
    clear()
    t = [40]
    interpreter(
"""
/x 10 def
/A { x } def
/C { /x 40 def A stack } def
/B { /x 30 def /A { x } def C stack} def
B
""", 'dynamic')
    if list(reversed(opstack)) != t:
        return False
    else:
        return True

		
		
def intertest4():
    print("~~~~~~~~~~~~~~~~~~~~~~TEST 4~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    clear()
    t = [24]
    interpreter(
"""
/z 8 def
/K { /x 3 def z x mul stack} def
K
""", 'static')
    if list(reversed(opstack)) != t:
        return False

			
    clear()
    t = [24]
    interpreter(
"""
/z 8 def
/K { /x 3 def z x mul stack} def
K
""", 'dynamic')
    if list(reversed(opstack)) != t:
        return False
    else:
        return True
		
		
def intertest5():
    print("~~~~~~~~~~~~~~~~~~~~~~TEST 5~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    clear()
    t = [100]
    interpreter(
"""
/s 97 def
/v 3 def
/P {s v add} def
P stack
""", 'static')
    if list(reversed(opstack)) != t:
        return False

			
    clear()
    t = [100]
    interpreter(
"""
/s 97 def
/v 3 def
/P {s v add} def
P stack
""", 'dynamic')
    if list(reversed(opstack)) != t:
        return False
    else:
        return True
				

def main_part2():
    testCases = [('inter1', intertest1), ('inter2', intertest2), ('inter3', intertest3), ('inter4', intertest4), ('inter5', intertest5)]
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All tests OK')	
	
if __name__ == '__main__':	
    print(main_part2())


	
	




