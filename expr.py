#Write a program to associate postfix notation of the given arithmetic expression with every node in the parse tree.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def checkOperator(op):
    return op in ['+', '-', '*', '/']

def constructTree(postFix):
    stack = []
    for token in postFix.split():
        if not checkOperator(token):
            stack.append(TreeNode(token))
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            rNode = stack.pop()
            lNode = stack.pop()
            opNode = TreeNode(token)
            opNode.left = lNode
            opNode.right = rNode
            stack.append(opNode)
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]

def parseTree(node, level=0, position="Root"):
    if node is not None:
        print('  ' * level + position + ": " + str(node.value))
        parseTree(node.left, level + 1, "Left")
        parseTree(node.right, level + 1, "Right")

def inToPostfix(expression):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}

    output = []
    opStack = []

    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            while opStack and opStack[-1] != '(':
                output.append(opStack.pop())
            opStack.pop()  
        else: 
            while opStack and prec.get(token, 0) <= prec.get(opStack[-1], 0):
                output.append(opStack.pop())
            opStack.append(token)
    while opStack:
        output.append(opStack.pop())
    return ' '.join(output)

infix = input("Enter arithmetic expr: ")
postfix = inToPostfix(infix)
parse_tree = constructTree(postfix)
print("Parse tree:")
parseTree(parse_tree)

#-----------------------------------------------

#2 Write a program to associate three address code of arithmetic expression (integer data types
#and mixed data types) with each node in the parse tree.
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.value)
    
class ThreeADC:
    def __init__(self):
        self.code = []
        self.tC = 0
        self.root = None

    def generate_temp(self):
        temp = "t"+str(self.tC)
        self.tC += 1
        return temp

    def generate_code(self, expr):
        lines=[]
        stack = []
        tokens = expr.split()
        for token in tokens:
            if token.isalnum():  
                stack.append(token)
            else: 
                op2 = stack.pop()
                op1 = stack.pop()
                temp = self.generate_temp()
                self.code.append((token, op1, op2, temp))
                stack.append(temp)
        for line in self.code:
            lines.append(line)
        return lines
            
    def generate_parse_tree(self, code):
        self.root = self.tree(code)

    def tree(self, code):
        stack = []
        for op, op1, op2, temp in code:
            node = TreeNode((op, temp))
            if op1.isdigit() or op1.isalpha():
                node.add_child(TreeNode(op1))
            else:
                node.add_child(stack.pop())

            if op2.isdigit() or op2.isalpha():
                node.add_child(TreeNode(op2))
            else:
                node.add_child(stack.pop())
            stack.append(node)
        return stack.pop()

    def print_tree(self, node, level=0):
        if node:
            print("  " * level + str(node))
            for child in node.children:
                self.print_tree(child, level + 1)
            
def inToPostfix(expression):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    opStack = []
    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            opStack.append(token)
        elif token == ')':
            while opStack and opStack[-1] != '(':
                output.append(opStack.pop())
            opStack.pop()  
        else: 
            while opStack and prec.get(token, 0) <= prec.get(opStack[-1], 0):
                output.append(opStack.pop())
            opStack.append(token)
    while opStack:
        output.append(opStack.pop())
    return ' '.join(output)

infix = "3 + 4 * ( 2 - 1 )"
postfix = inToPostfix(infix)

code = ThreeADC()

lines=code.generate_code(postfix)
code.generate_parse_tree(lines)
code.print_tree(code.root)

'''
#-------------------------------------------

#Write a program to associate three address code of Boolean expressions (involving relational
#operators, “and”, ”or” and not) with each node in the parse tree.
'''
def inToPostfix(expression):
    prec = {'NOT': 3, 'AND': 2, 'OR': 1}
    associativity = {'NOT': 'right', 'AND': 'left', 'OR': 'left'}
    output = []
    opStack = []
    tokens = expression.split()
    for token in tokens:
        if token not in ['NOT','AND','OR']: 
            output.append(token)
        else:
            while (opStack and
                   prec.get(token, 0) <= prec.get(opStack[-1], 0) and
                   (associativity[token] == 'left' or prec[token] < prec[opStack[-1]])):
                output.append(opStack.pop())
            opStack.append(token)
    while opStack:
        output.append(opStack.pop())
    return ' '.join(output)
    
class ThreeADC:
    def __init__(self):
        self.root = None
        self.code = []
        self.tC = 0
        
    def getTempvar(self):
        temp = "t"+str(self.tC)
        self.tC += 1
        return temp

    def parseTree(self, expr):
        stack = []
        relOp = expr.split()
        for token in relOp:
            if token == 'NOT':  
                op = stack.pop()
                temp = self.getTempvar()
                self.code.append(('NOT', op, temp))
                stack.append(temp)
            elif token in ['AND', 'OR']:  
                op2 = stack.pop()
                op1 = stack.pop()
                temp = self.getTempvar()
                self.code.append((token, op1, op2, temp))
                stack.append(temp)
            else:  
                stack.append(token)
        for l in self.code:
            print(l)

expr = "NOT b AND c AND d"
postfix = inToPostfix(expr)
code = ThreeADC()
code.parseTree(postfix)
'''