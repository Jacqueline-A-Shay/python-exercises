import matplotlib
import matplotlib.pyplot as plt

x = range(1, 5)
y = x
plt.scatter(x, y)
plt.yticks([1, 2, 3, 4], ['one', 'two', 'three', 'four'], rotation=45)
#alternative: plt.yticks(y, ['one', 'two', 'three', 'four'], rotation=45)
plt.xticks(rotation=45)
plt.show()

plt.close() #free up memory space, close down all the special design for your fig


# plot the first subplot
plt.subplot(121) # 1 row, 2 columns, the 1st column
plt.plot(x, y)
plt.title('x ~ y')

plt.scatter(range(len(x1)), x1, s=30, c='red') # s = point size 
plt.scatter(range(len(x2)), x2, s=10, c='green') # c = color of the line or in this case point
plt.show()