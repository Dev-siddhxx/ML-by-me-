import numpy as np
import matplotlib.pyplot as plt 
# to find the value of the sin in numpy library we do the following 
an1 = np.sin(180)
print(an1)


print(np.sin(90))

# to find the value fo dcos in the numpy library we do the following 
print(np.cos(90))

# in same way in order to do the thing with tan we do the following 


print(np.tan(45))

# in order to plot sinx , siny graph using matplotlib we do the following 

sin_x = np.arange(0,3*np.pi, 0.1)# for the x axis 
sin_y = np.sin(sin_x)


print(sin_y)


plt.plot(sin_x, sin_y)
plt.show()




# in order to plot cos graph we do the following 
cos_y = np.cos(sin_x)
plt.plot(sin_x, cos_y)
plt.show()

# same way in order to do tan we do the following 
tan_y = np.tan(sin_x)
plt.plot(sin_x, tan_y)
plt.show()
