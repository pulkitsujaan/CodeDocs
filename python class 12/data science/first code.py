import matplotlib.pyplot as plt

input_values=[1,2,3,4,5]
squares=[1,4,9,16,25]

# setting styles
'''
to set styles and check which is available, run this command in terminal
import matplotlib.pyplot as plt
plt.style.available
'''
plt.style.use('seaborn-v0_8-dark')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Customization
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis='both',labelsize=14)# Size of tick labels


plt.show()