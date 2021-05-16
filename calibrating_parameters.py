# Comparing with literature is an approximation because the settings used in literature 
# and in agent based modeling are not totally same.

# The results in literature depends on type of fluid, diameter of glass, temperature etc.

# I have assumed that V(t) ~ C*NumberOfBubbles(t)
# Here, the time scale could vary in real-life vs in Netlogo
# The above formula, may depend on other factors as well used in the literature


# Importing modules
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import seaborn as sns
import math
sns.set()

# Values obtained in literature
original_a = 3.64
original_b = 0.00434
original_c = 0.00000066

# Value for C
C = 0.019046

# Opening the file and reading from 8th line
input_file = open('number_of_bubbles_for_comparing_with_literature.csv')
lines = input_file.readlines()[7:]

# Arrays to store various values
number_of_bubbles = [i for i in range(1, 401)]
volume_of_bubbles_in_log = [i for i in range(1, 401)]
x_axis = [i for i in range(1, 401)]

# Reading the input
for line in lines:

    # Converting values in line to integer form
    values = line.strip().lstrip().split(",")
    for i in range(len(values)):        
        values[i] = int(values[i][1:len(values[i])-1])        

    [run_number,incoming_bubble_rate,increase_size_probability_if_collide,probability_of_collision,initial_bubble_number,step,number_of_turtles] = values

    # Number of bubbles at time step
    number_of_bubbles[step-1] = number_of_turtles

    # Assuming that V(t) = C*NumberOfBubbles(t)
    # Since, V(0) = 38.092 and N(0) = 2000 => C = 0.019046
    # Converting V(t) to log(V(t)), log(V(t)) = log(C) + log(NumberOfBubbles(t))    
    volume_of_bubbles_in_log[step-1] =  math.log(C) + math.log(number_of_bubbles[step-1])


# Fitting function
def fitting_function(t, a, b, c):    
    return a - b*t - c*(t**2.5)


# Fitting using Curve Fit function of Scipy modules
[a, b, c], Pcov = curve_fit(fitting_function, x_axis, volume_of_bubbles_in_log)


# Plotting Volume V(t) vs t



# Value obtained by agent based modeling 
# V(t) = C*NumberOfBubble(t)
plt.plot(x_axis, [C*val for val in number_of_bubbles], label = "Agent Based Model")

# Value obtained by fitting values of agent based modeling in the equation of form 
# V(t) = exp(a - b*t - c*(t**2.5))
plt.plot(x_axis, [math.exp(fitting_function(val, a, b, c)) for val in x_axis], label = "Fitting (a="+str(a)[:4]+", b="+("{:.2e}".format(b))+", c="+("{:.2e}".format(c))) 

# Value obtained in literatue 
# V(t) = exp(original_a - original_b*t - original_c*(t**2.5))
plt.plot(x_axis, [math.exp(fitting_function(val, original_a, original_b, original_c)) for val in x_axis], label = "Literature (a="+str(original_a)+", b="+("{:.2e}".format(original_b))+", c="+("{:.2e}".format(original_c))+"")        

plt.ylabel('V(t)')
plt.title('Comparing with Literature')
plt.xlabel('t')
plt.legend()
plt.savefig('literature_comparison.png',dpi=720)   

