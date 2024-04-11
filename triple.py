# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:14:04 2024

@author: maana
"""

class exprConv: 
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
     
    def isEmpty(self):
        return True if self.top == -1 else False
     
    def peek(self):
        return self.array[-1]
     
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
     
    def push(self, op):
        self.top += 1
        self.array.append(op) 
 
    def isOperand(self, ch):
        return ch.isalpha()
 
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError: 
            return False
             

    def infixToPostfix(self, exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
 
            elif i == ')':
                while( (not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
 
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i) 
        while not self.isEmpty():
            self.output.append(self.pop())
        #print("Postfix notation")
        #print ("".join(self.output))
        return "".join(self.output)
    

def ThreeADC(exp):
        tempSp = ''
        for i in exp:
            if i != " ":
                tempSp += i

        exp = tempSp
        stack = []
        x = 1
        obj = exprConv(len(exp))
        postfix = obj.infixToPostfix(exp)
        for i in postfix:
            if i.isalpha() or i.isdigit():
                stack.append(i)
            elif i == '-':
                op1 = stack.pop()
                print("t(",x,")","=",i,op1)
                stack.append("t(%s)" %x)
                x = x+1
                if stack != []:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    print("t(",x,")","=",op1,"+",op2)
                    stack.append("t(%s)" %x)
                    x = x+1
            elif i == '=':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    print(op1,i,op2)

            else:
                op1 = stack.pop()
                if stack !=[]:
                        op2 = stack.pop()
                        print("t(",x,")","=",op2,i,op1)
                        stack.append("t(%s)" %x)
                        x = x+1
def Quadruple(exp):
        tempSp = ''
        for i in exp:
            if i != " ":
                tempSp += i

        exp = tempSp
        stack = []
        x = 1
        obj = exprConv(len(exp))
        postfix = obj.infixToPostfix(exp)
        print("{0:} | {1:} | {2:} | {3:}".format('op','arg1','arg2','result'))
        for i in postfix:
            if i.isalpha() or i.isdigit():
                stack.append(i)
            elif i == '-':
                op1 = stack.pop()
                stack.append("t(%s)" %x)
                print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op1,""," t(%s)" %x))
                x = x+1
                if stack != []:
                    op2 = stack.pop()
                    op1 = stack.pop()
                    print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format("+",op1,op2," t(%s)" %x))
                    stack.append("t(%s)" %x)
                    x = x+1
            elif i == '=':
                    op2 = stack.pop()
                    op1 = stack.pop()
                    print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op2,"",op1))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                print("{0:^4s} | {1:^4s} | {2:^4s}|{3:4s}".format(i,op2,op1," t(%s)" %x))
                stack.append("t(%s)" %x)
                x = x+1


def Triple(exp):
    tempSp = ''
    for i in exp:
        if i != " ":
            tempSp += i

    exp = tempSp
    stack = []
    x = 0
    obj = exprConv(len(exp))
    postfix = obj.infixToPostfix(exp)
    print("{0:^4s} | {1:^4s} | {2:^4s}".format('op', 'arg1', 'arg2'))
    for i in postfix:
        if i.isalpha() or i.isdigit():
            stack.append(i)
        elif i == '-':
            op1 = stack.pop()
            stack.append("(%s)" % x)
            print("{0:^4s} | {1:^4s} | {2:^4s}".format(i, op1, ""))
            x = x + 1
            if stack != []:
                op2 = stack.pop()
                op1 = stack.pop()
                print("{0:^4s} | {1:^4s} | {2:^4s}".format("+", op1, op2))
                stack.append("(%s)" % x)
                x = x + 1
        elif i == '=':
            op2 = stack.pop()
            op1 = stack.pop()
            print("{0:^4s} | {1:^4s} | {2:^4s}".format(i, op1, op2))
        else:
            op1 = stack.pop()
            if stack != []:
                op2 = stack.pop()
                print("{0:^4s} | {1:^4s} | {2:^4s}".format(i, op2, op1))
                stack.append("(%s)" % x)
                x = x + 1

#exp = input("Enter a valid infix expression  \n")

exp = 'x=(a^b)*c/d'

print("Three ADC : ")
ThreeADC(exp)
print("In quadruple form : ")
Quadruple(exp)
print("In Triplet form: ")
Triple(exp)