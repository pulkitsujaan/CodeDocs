import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()


# #first five cubic numbers
# num=[1,2,3,4,5]
# cubes=[1,8,27,64,125]

# ax.plot(num,cubes)
# ax.set_title("Cubes",fontsize=14)
# ax.set_xlabel("Number",fontsize=14)
# ax.set_ylabel("Value",fontsize=14)
# ax.tick_params(axis='both',labelsize=14)
# plt.show()



#5000 numbers
num=range(1,5001)
cubes=[x*x*x for x in num]
# ax.scatter(num,cubes,s=10,c=(0,0.6,0.4))
ax.scatter(num,cubes,c=cubes,cmap=plt.cm.winter,s=10)
ax.set_title("Cubes",fontsize=14)
ax.set_xlabel("Number",fontsize=14)
ax.set_ylabel("Value",fontsize=14)
ax.tick_params(axis='both',labelsize=14)
plt.show()