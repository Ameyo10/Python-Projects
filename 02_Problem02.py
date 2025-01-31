'''
Finding the depth upto which the solid spherical ball is submerged in the water
'''
import matplotlib.pyplot as plt
d0=1
r=10
rho= 0.638
class newton_raphson:
    def __init__(self,d0,r,rho):
        self.d0= d0
        self.r=r
        self.rho=rho
        self.d1=0.0

    def fun(self):    #Function for the depth upto which the ball is submerged
        return self.d0**3 - 3*self.r*(self.d0**2)+ 4*(self.r**3)*self.rho
    def der_fun(self):     #Derivative of the function for the depth upto which the ball is submerged
        return 3*(self.d0**2) - 6*self.r*self.d0+ 12*(self.r**2)*self.rho
    def main(self):      #Using Newton- Raphson Method to find the depth
        while abs(self.d1-self.d0)>= (10**-5):
            self.d1=self.d0-(self.fun()/self.der_fun())
            self.d0=self.d1
        return self.d1
print (f'The depth upto which the spherical ball gets submerged is {abs(newton_raphson(d0,r,rho).main()):6f} cm')

# List to store values for plotting
d0_values = [i for i in range(1, 11)] 
depth_values = []

# Compute the depth for each d0
for d0 in d0_values:
    depth = abs(newton_raphson(d0, r, rho).main())  # Use absolute value
    depth_values.append(depth)

# Plotting the results
plt.plot(d0_values, depth_values, marker='o')
plt.title('Depth of Submersion vs. Initial Guess d0')
plt.xlabel('Initial Guess d0 (cm)')
plt.ylabel('Submersion Depth (cm)')
plt.grid(True)
plt.show()