
import sys

stack=[]
symbol=[]
inp=[]


mainList=[]
ruleList=[]
parseTable=[]
grammar=[]
filled=[]

def is_terminal(character):
	#check if input character is smaller letter of not
	if character.isupper():
		return False
	else:
		return True

def compute_first(X): # computing first for the grammar
	first = []	
	#if X=="":
	#	return X
	#print(X)
	if is_terminal(X):
			first.append(X)
			#print("here")
			return first

	for i in grammar:
		#print(X," loop ",i)
		#print(i[0])
		if i[0] == X:
			#print("here")
			if i[1] != i[0]: 
				next_term = i[1]
				if is_terminal(next_term):
					# print "here"
					if not(next_term in first):
						first.append(next_term)
				else:
					p=compute_first(next_term)
					for q in p:
						if not(q in first):
							first.append(q)
	return first

def compute_follow(X): #calculating follow 
	follow = []
	if X == grammar[0][1]:
		follow.append('$')
		#return follow
	for j in grammar:	
		if X in j[1:]:
			for i in range(0,len(j[1:])):
				if X == j[1:][i]:
					# print X, i.index(X), len(i)
					#print(j," ::: ",j[1:].index(X)," ::: ",X)
					if i == len(j[1:])-1:
						# print "lst"
						if not j[0] == X:
							temp_follow = compute_follow(j[0])
							# print temp_follow
							for k in temp_follow:
								if not(k in follow):
									follow.append(k)
						continue

					temp_first = compute_first(j[1:][i+1])				
					#print(temp_first)
					for k in temp_first:
						if not (k in follow):
							follow.append(k)
	return follow


def shift(per,i):
	stack.append(int(per[1:]))
	symbol.append(i)
	print('Current Stack : ',stack)	


def rduce(per,rl,alpha,table):
	r=int(per[1:])
	print("S"+str(per[1:]))
	rule=rl[r]
	r1=rule.split(':')[1].strip()
	r1=r1.split(' ')
	l=len(r1)
	s=symbol[-l:]
	s=''.join(s)
	for i in range(0,l):
		stack.pop()	
		symbol.pop()
		print(symbol, end="\t")
	sym=rule.split(':')[0]
	symbol.append(sym)
	index=alpha.index(sym)
	a=table[stack[-1]][index]
	stack.append(a)
	print('Current Stack : ',stack)
    
    
def parse(inpt,table,alpha,rl):
	i = int(alpha.index('$')+1)
	term = alpha[0:i]
	l = len(term)
	inp = inpt.strip().split(' ')
	inp.append('$')
	for i in inp:
		if i not in term:
			print("Inalid input:",i)
			exit(0)
	stack.append(0)
	try:
		i=0
		
		while i<len(inp):
			inpt=inp[i]
			index=term.index(inpt)
			per=table[stack[-1]][index]
			if per=='accept':
				print('SLR Parsing successful.')	
				break
			elif per[0]== 's':
				print("Shift", end='\t')
				shift(per,inpt)
				i+=1
			elif per[0]== 'r':
				print("reduce", end='\t')
				rduce(per,rl,alpha,table)	
			print("\n")
	except:
		print('Invalid input. SLR parsing failed')
		exit(0)
        
        


def alphabet():
	alpha=[]
	for gra in ruleList:
		#print(gra)
		gra=gra.split(':')[1].strip()
		#print(gra)
		l=gra.split(' ')
		#print(l)
		for i in l:
			if i not in alpha:
				if i.isupper():
					alpha.append(i)								
				else:
					alpha.insert(0,i)
	return alpha

def div():
	for x in ruleList:
		l=x.split(' ')
		l[0]=l[0].strip(':')
		grammar.append(l)
	return 

def L0Sets(alpha):
	
	I0=[ruleList[0]]
	I0=appendS(I0)	
	mainList.append(I0)
	i=0;
	while i<len(mainList):
		state(mainList[i],alpha)
		i+=1
	slrptable(alpha)
	

def state(I,alpha):
	l=[]
    
	for a in alpha:
		subl=[]
		f=0
		for r in I:
			if r.split(':')[1].strip().split(' ')[0]==a:
				if a == '$':
				        f=1
				elif r in ruleList:
					s=r.split(':')[0]+': '+' '.join(r.split(' ')[2:])+' /{}'.format(ruleList.index(r))
					subl.append(s)
				else:
					s=r.split(':')[0]+': '+' '.join(r.split(' ')[2:])
					subl.append(s)				
				
		if len(subl)>0:
			subl=appendS(subl)		
			if subl not in mainList:			
				mainList.append(subl)

		if f==0:
			l.append(subl)
		else:
			l.append(['A'])
						
	ptable(l,alpha)
	

def ptable(l,alpha):
	p=len(parseTable)
	parseTable.append([])
	filled.append([])
	if all(i==[] for i in l):
		rule=mainList[p][0]
		rule=rule.split('/')[1].strip()
		for i in range(0,len(alpha)):
			lst = compute_follow(grammar[int(rule)][0])
			#print(lst)
			if len(parseTable[p])<(alpha.index('$')+1):
				#print(alpha[len(parseTable[p])])
				if alpha[len(parseTable[p])] in lst:
					parseTable[p].append('r'+rule)
					filled[p].append(2);
				else:
					parseTable[p].append(0)
					filled[p].append(0);
			else:
				parseTable[p].append(0)
				filled[p].append(0);
	else:
		for i in l:			
			if i == ['A']:
				parseTable[p].append('accept')
			elif i == []:
				parseTable[p].append(0)
				filled[p].append(0);
			else:
				if len(parseTable[p])<(alpha.index('$')+1):
					parseTable[p].append('s'+str(mainList.index(i)))
					filled[p].append(1);
				else:
					parseTable[p].append(mainList.index(i))
					filled[p].append(0);

		
def slrptable(alpha):
	for st in mainList:
		flag=0
		cnt=[]
		for s in st:
			if s.split(':')[1].split('/')[0].strip()=='':
				rule=s.split('/')[1]
				flag=1
				#print(mainList.index(st))
				#print(ruleList[int(rule)])
				#break;
				cnt.append(rule)
		if(flag==1):
			for x in cnt:
				lst = compute_follow(grammar[int(x)][0])
				for i in range(0,((alpha.index('$')+1))):
					if alpha[i] in lst:
						if filled[mainList.index(st)][i] == 0:
							parseTable[mainList.index(st)][i]='r'+x

def appendS(s):
	for j in range(1,len(ruleList)):
			i=s[(len(s)-1)]
			a=i.split(':')[1].strip()
			a=a.split(' ')[0]
			for r in ruleList:
				if r.split(':')[0].strip() == a:
					s.append(r)
	return s
	

def main():
	r=0
	f=open('grammar2.txt','r')
	rule=f.readline()
	while rule:
		r+=1
		rule=rule.strip()
		ruleList.append(rule)
		rule=f.readline()
	s=''.join(['S1: ',ruleList[0].split(':')[0].strip(),' $'])
	ruleList.insert(0,s)
	print("\nGrammer list:",ruleList)
	div()
	alpha=alphabet()
	print("\nTerminal and nonterminal:",alpha)

	L0Sets(alpha)
	print("\nStates:")
	j=0
	for i in mainList:
		print("I{}: ".format(j),i)
		j+=1
		
	print("\nParsing Table:\n")
	j=0
	print("\t\t",end="")
	for ele in alpha:
		print(ele,"\t",end="")
		
	print()
	print("******************************************** ")

	for i in parseTable:
		print("{}\t|\t".format(j),end="")
		for ind in i:
			if ind == 0:
				ind =""
			print(ind,"\t",end="")
		#print("{}\t|\t".format(j),i)
		print()
		print("----------------------------------------------")
		j+=1
	
	inpt=input("Enter string to be parsed  (Ex: id * id)):\n")
	parse(inpt, parseTable, alpha, ruleList)

num=0
main()
