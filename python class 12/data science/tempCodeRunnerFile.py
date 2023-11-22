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
rw=RandomWalk(50_000)
rw.fill_walk()
