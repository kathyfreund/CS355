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
		dictstack.append(d)
	else:
		(dictstack[-1])[name] = value
 

def lookup(name):
    name = '/' + name
    for d in reversed(dictstack):
        if name in d:
            return d[name]
        else:
            print()
			#print("[!] ERROR - Name does not exist in any dictionary.")

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
				interpret(arr)
		elif i < 0:
			#print("BREAKPOINT")
			for z in range(x, f, i):
				#print(x)
				opPush(z)
				interpret(arr)
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
	
def stack():
	print(opstack)
	
#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef

def psDict():
	opPop() #MESSED UP DURING PART 1, answer to all my prayers?
	nd = {}
	opPush(nd)
	
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
		
def begin():
	op1 = opPop()
	if isinstance(op1, dict):
		dictPush(op1)
	else:
		print("[!] ERROR - Not a dictionary.")
	
def end():
	dictPop()

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


def interpret(code):
	mop = {"dup": dup, "exch": exch, "pop": pop, "roll": roll, "copy": copy, "clear": clear, "stack": stack, "add": add, "sub": sub, "mul": mul, "div": div, "mod": mod, "def": psDef, "dict": psDict, "begin": begin, "end": end, "length": length, "get": get, "for": psFor}
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
				look = lookup(c)
				if look != None:
					if isinstance(look, list):
						interpret(look)
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

def interpreter(s):
	interpret(parse(tokenize(s)))

	
#------- Part 1 TEST CASES--------------

def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opstack)
    opPush(10)
    pop()
    l2= len(opstack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opstack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True
    

#------- Part 2 TEST CASES--------------

def testparse1():
    t = ['/square',['dup','mul'],'def',1,'square',2,'square', 3,'square','add','add']
    t1 = (parse(tokenize(
"""
/square {dup mul} def 1 square 2 square 3 square add add
"""
)))
    if t != t1:
        return False
    else:
        return True

		
def testparse2():
    t = ['/n', 5, 'def', 1, 'n', -1, 1, ['mul'], 'for']
    t1 = (parse(tokenize(
"""
/n 5 def 1 n -1 1 {mul} for
"""
)))
    if t != t1:
        return False
    else:
        return True


		
def testparse3():
    t = ['/sum', [-1, 0, ['add'], 'for'], 'def', 0, [1, 2, 3, 4], 'length', 'sum', 2,
'mul', [1, 2, 3, 4], 2, 'get', 'add', 'add', 'add', 'stack']
    t1 = (parse(tokenize(
"""
/sum { -1 0 {add} for} def
 0
 [1 2 3 4] length
 sum
 2 mul
 [1 2 3 4] 2 get
 add add add
 stack
"""
)))
    if t != t1:
        return False
    else:
        return True

		
		
def testparse4():
    t = ['/fact', [0, 'dict', 'begin', '/n', 'exch', 'def', 1, 'n', -1, 1,
['mul'], 'for', 'end'], 'def', [1, 2, 3, 4, 5], 'dup', 4, 'get',
'pop', 'length', 'fact', 'stack']
    t1 = (parse(tokenize(
"""
/fact{
 0 dict
 begin
 /n exch def
 1
n -1 1 {mul} for
 end
 }def
 [1 2 3 4 5] dup 4 get pop
 length
 fact
 stack
"""
)))
    if t != t1:
        return False
    else:
        return True
		

		
def intertest1():
    t = 14
    interpreter(
"""
/square {dup mul} def 1 square 2 square 3 square add add
stack
""")
    if opPop() != t:
        return False
    else:
        return True
		

		
def intertest2():
    t = 120
    interpreter(
"""
/n 5 def 1 n -1 1 {mul} for
stack
""")
    if opPop() != t:
        return False
    else:
        return True
		

def intertest3():
    t = 23
    interpreter(
"""
 /sum { -1 0 {add} for} def
 0
 [1 2 3 4] length
 sum
 2 mul
 [1 2 3 4] 2 get
 add
 stack
""")
    if opPop() != t:
        return False
    else:
        return True


		
def intertest4():
    t = 120
    interpreter(
"""
 /fact{
 0 dict
 begin
 /n exch def
 1
n -1 1 {mul} for
 end
 }def
 [1 2 3 4 5] dup 4 get pop
 length
 fact
 stack
""")
    if opPop() != t:
        return False
    else:
        return True
		
		

def main_part2():
    testCases = [('parse1', testparse1), ('parse2', testparse2), ('parse3', testparse3), ('parse4', testparse4), ('inter1', intertest1), \
				('inter2', intertest2), ('inter3', intertest3), ('inter4', intertest4)]
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-2 tests OK')
	
	
def main_part1():
    testCases = [('define',testDefine),('lookup',testLookup),('add', testAdd), ('sub', testSub),('mul', testMul),('div', testDiv),  ('mod', testMod), \
                ('length', testLength),('get', testGet), ('dup', testDup), ('exch', testExch), ('pop', testPop), ('roll', testRoll), ('copy', testCopy), \
                ('clear', testClear), ('dict', testDict), ('begin', testBeginEnd), ('psDef', testpsDef), ('psDef2', testpsDef2)]
    # add you test functions to this list along with suitable names
    failedTests = [testName for (testName, testProc) in testCases if not testProc()]
    if failedTests:
        return ('Some tests failed', failedTests)
    else:
        return ('All part-1 tests OK')
	
	
if __name__ == '__main__':	
    print(main_part1())
    print(main_part2())


	
	




