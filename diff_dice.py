#different dice
#dice visual
import pygal
from die import Die

#create a D6 and a D10
die_1 = Die()
die_2 = Die(10)


#make rolls, store results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualize the results
hist = pygal.Bar()
exlabels = []
for num in range(2, 17):
    exlabels.append(num)

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = exlabels
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
