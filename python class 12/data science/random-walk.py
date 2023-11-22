from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    '''Random Walks'''
    def __init__(self,num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #move that go nowhere
            if x_step==0 and y_step==0:
                continue

            # new position
            x=self.x_values[-1]+x_step
            y=self.y_values[-1]+y_step

            self.x_values.append(x)
            self.y_values.append(y)


# while True:

#     rw=RandomWalk()
#     rw.fill_walk()
#     fig, ax=plt.subplots()
#     ax.scatter(rw.x_values,rw.y_values,s=15,color='green')
#     plt.show()

#     run=input("Make another input?(y/n)  ")
#     if run=='n':
#         break


# rw=RandomWalk()
rw=RandomWalk()
rw.fill_walk()

fig, ax=plt.subplots()
plot_numbers=range(rw.num_points)

ax.scatter(rw.x_values,rw.y_values,c=plot_numbers,cmap=plt.cm.Blues,s=15,edgecolors='none')

# starting and end points bigger and of different colors
ax.scatter(0,0,c='green',edgecolors='none',s=100)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

#removing axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()