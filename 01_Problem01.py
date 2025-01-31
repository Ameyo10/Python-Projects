'''
Use Secant and Muller method to solve cosx= x^2+x upto 5 decimal places
'''
import math
x0=1
x1=2
x2=4

# function

def fun(x):
    return math.cos(x)-(x**2)-x

# Secant method

def Secant_method(x0,x1,tol=(10**-5)):
    y=0.0
    while abs(x1-x0)>=tol:
        y=x1-((x1-x0)/(fun(x1)-fun(x0)))*fun(x1)
        x0,x1=x1,y
    
    return y

# Muller method

class Muller_method:
    def __init__(self, x0,x1,x2):
        self.x0=x0
        self.x1= x1
        self.x2= x2
        self.x3= 0.0
    def h(self,p,q):
        return p-q
    def delta(self,p,q):
        return (fun(p)-fun(q))/self.h(p,q)
    def a(self):
        return (self.delta(self.x2,self.x1)-self.delta(self.x1,self.x0))/(self.h(x2,x1)-self.h(x1,x0))
    def b(self):
        return self.a()*self.h(self.x2,self.x1)+self.delta(self.x2,self.x1)
    def c(self):
        return fun(self.x2)
    def main(self):
        while abs(self.x3-self.x2)>=(10**-5):
            self.x3 = self.x2 +((-2*self.c())/(self.b()**2)-4*self.a()*self.c())**0.5
            self.x0,self.x1,self.x2=self.x1,self.x2,self.x3
        return self.x3
    
# Result
print(f'The solution of the expression f(x)=cos x - x^2 - x by Secant method is {Secant_method(x0,x1):.5f}')
print(f'The solution of the expression f(x)=cos x - x^2 - x by Muller method is {Muller_method(x0,x1,x2).main():.5f}')