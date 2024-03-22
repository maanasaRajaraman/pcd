#slr.txt
#start E 
#E->E+E 
#E->E-E 
#E->E*E 
#E->E/E 
#E->i 
#terminals [+,-,*,/,i]


from collections import *

file=open("slr.txt","r")

flag = False
nT = []
T = []
handles = []
initial_production = {}
productions = defaultdict(list)
startSymbol = ""

for line in file:
  l = line.strip()
  if("start" in line):
    s1 = l.split()
    startSymbol = s1[1]
    continue

  if ("terminals" in line):
    s1 = line.split()
    lis = s1[1]
    new_lis = lis[1:-1]
    final_lis = new_lis.split(',')
    T.extend(final_lis)
    continue

  s1=l.split("->")
  left = s1[0]
  if(left not in nT):
    nT.append(left)

  right = s1[1]
  productions[left].append(right)
  if left==startSymbol:
    handles.append(right)


ipStr = input("\nEnter the string to be parsed: ")

ipBuffer = deque()
for c in ipStr:
  ipBuffer.append(c)
ipBuffer.append('$')

stack=[]

print("\n\n")
print("Curr-Stack\t\t\tInput-Buffer\t\t\t Action")
print("\n")

stack.append('$')

print(stack, end='\t\t\t')
print(list(ipBuffer), end='\t\t')
print("Shift")


stack.append(ipBuffer.popleft())

stackEnd = ['$', startSymbol]
buffEnd=['$']

while(ipBuffer):
  st=""
  endIndex = len(stack)
  i=len(stack)-1
  while(i!=0):
      st += stack[i]
      if(st in handles):
        startIndex=i
        print(stack, end='\t\t')
        appendStack = stack
        stack[startIndex:endIndex] = startSymbol
        i=len(stack)-1

        print(list(ipBuffer),end='\t\t')
        print("Red E->",st)
        st=""
        print("\n")  
      else:
        i-=1

  if(stack == stackEnd and list(ipBuffer) == buffEnd):
    flag = True
    print(stack,end="\t\t\t")
    print(list(ipBuffer),end="\t\t\t")
    print("Accept") 
    break

  print(stack,end='\t\t')
  print(list(ipBuffer),end='\t\t')
  print("Shift") 
  stack.append(ipBuffer.popleft())

if(flag == False):
  print("\n\n\t\tString not accepted !")


column_widths = [max(len(str(item)) for item in column) for column in zip(*finalRes)]
 
for column, width in zip(finalRes[0], column_widths):
    print(f"{column:{width}}", end=" | ")
print()
 
print("-" * (sum(column_widths) + len(column_widths) * 3 - 1))
 
for row in finalRes[1:]:
    for item, width in zip(row, column_widths):
        if isinstance(item, list):
            print(f"{str(item):{width}}", end=" | ")
        else:
            print(f"{item:{width}}", end=" | ")
    print()
