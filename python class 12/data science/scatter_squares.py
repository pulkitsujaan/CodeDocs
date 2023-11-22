import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
# ax.scatter(2,4)

# ax.scatter(2,4, s=200)# s parameter increases size of the dots
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(axis='both',which='major', labelsize=14)# Size of tick labels



# #using multiple values
# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]
# ax.scatter(x_values,y_values,s=100)


# using loops
x=range(1,1001)
y=[x**2 for x in x]
# ax.scatter(x,y,s=10)
# ax.axis([0,1100,0,11_00_000])#defining range for both axes


# ax.scatter(x,y,c='red',s=10)#for colored points
# ax.scatter(x,y,c=(0,0.4,0),s=10)#for colored points(RGB method)
# ax.axis([0,1100,0,11_00_000])

ax.scatter(x,y,c=y,cmap=plt.cm.Blues,s=10)#colormap
# plt.show()


# to automatically save plots, replace plot.show() with plot.savefig()
plt.savefig('squares_plot.png',bbox_inches='tight')