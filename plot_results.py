import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# Number of Bubble Curves by Varying Probability of Collision
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Reading the input from 8th line
input_file = open('number_of_bubbles_with_param_probability_of_collision.csv')
lines = input_file.readlines()[7:]

# Dictionary to store number of bubbles for each probability 
number_of_bubbles = dict()

# Initiliazing arrays
probability_of_collision = 0
x_axis = [i for i in range(1, 301)]

while probability_of_collision<=100:
    number_of_bubbles[probability_of_collision] = [0]*300
    probability_of_collision+=10

for line in lines:

    # Converting values in line to integer form
    values = line.strip().lstrip().split(",")
    for i in range(len(values)):        
        values[i] = int(values[i][1:len(values[i])-1])  

    [run_number,incoming_bubble_rate,increase_size_probability_if_collide,probability_of_collision,initial_bubble_number,step,number_of_turtles] = values

    # Assign value for respective probability and time step
    number_of_bubbles[probability_of_collision][step-1] = number_of_turtles


plt.figure(1)

alpha = 0.1
# Plotting all curves one-by-one
for probability_of_collision in number_of_bubbles:
    plt.plot(x_axis, number_of_bubbles[probability_of_collision], label = str(probability_of_collision), color = (0.8313, 0, 1, alpha))        
    alpha+=0.09

plt.ylabel('Number of Bubbles')
plt.title('Number of Bubbles Curves by Varying Probability of Collision')
plt.xlabel('Time Steps')
plt.legend()
plt.savefig('number_of_bubbles_with_param_probability_of_collision.png',dpi=720)    


# Average Radius of Bubble Curves by Varying Probability of Increasing Size
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

input_file = open('average_radius_of_bubbles_with_param_increase_size_probability.csv')
lines = input_file.readlines()[7:]

average_radius = dict()

probability_of_increasing_size = 0
x_axis = [i for i in range(1, 501)]

while probability_of_increasing_size<=100:
    average_radius[probability_of_increasing_size] = [0]*500
    probability_of_increasing_size+=10

for line in lines:
    values = line.strip().lstrip().split(",")
    for i in range(len(values)):        
        values[i] = float(values[i][1:len(values[i])-1])        
    [run_number,incoming_bubble_rate,probability_of_increasing_size,probability_of_collision,initial_bubble_number,step,average_radius_of_bubbles] = values    
    average_radius[int(probability_of_increasing_size)][int(step)-1] = average_radius_of_bubbles

plt.figure(2)


alpha = 0.1
for probability_of_increasing_size in average_radius:
    plt.plot(x_axis, average_radius[probability_of_increasing_size], label = str(probability_of_increasing_size), color = (0, 0.66, 1, alpha))        
    alpha+=0.09

plt.ylabel('Average Radius of Bubbles')
plt.title('Average Radius of Bubble Curves by Varying Probability of Increasing Size')
plt.xlabel('Time Steps')
plt.legend()
plt.savefig('average_radius_of_bubbles_with_param_increase_size_probability.png',dpi=720)    





# Number of Bubble Curves by Varying Incoming Bubble Rate
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

input_file = open('number_of_bubbles_with_param_incoming_bubble_rate.csv')
lines = input_file.readlines()[7:]

number_of_bubbles = dict()

incoming_bubble_rate = 0
x_axis = [i for i in range(1, 301)]

while incoming_bubble_rate<=100:
    number_of_bubbles[incoming_bubble_rate] = [0]*300
    incoming_bubble_rate+=10

for line in lines:
    values = line.strip().lstrip().split(",")
    for i in range(len(values)):        
        values[i] = int(values[i][1:len(values[i])-1])        
    [run_number,incoming_bubble_rate,increase_size_probability_if_collide,probability_of_collision,initial_bubble_number,step,number_of_turtles] = values
    number_of_bubbles[incoming_bubble_rate][step-1] = number_of_turtles


plt.figure(3)

alpha = 0.1
for incoming_bubble_rate in number_of_bubbles:
    plt.plot(x_axis, number_of_bubbles[incoming_bubble_rate], label = str(incoming_bubble_rate), color = (0.998, 0.2862, 0.0117, alpha))        
    alpha+=0.09

plt.ylabel('Number of Bubbles')
plt.title('Number of Bubbles Curves by Incoming Bubble Rate')
plt.xlabel('Time Steps')
plt.legend()
plt.savefig('number_of_bubbles_with_param_incoming_bubble_rate.png',dpi=720)    