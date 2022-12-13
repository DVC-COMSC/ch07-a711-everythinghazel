import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2

# ******************************
fig,ax = plt.subplots()
Math = ax.bar(x-width*1.5,Math,width)
English = ax.bar(x-width*1.5,English,width)
Physics = ax.bar(x+width*1.5,Physics,width)
Computer = ax.bar(x+width*1.5,Computer,width)

ax.legend(["Math", "English", "Physics", "Computer"])

ax.set_title("Grouped graph for scores")

ax.bar_label(Math,Math)
ax.bar_label(English,English)
ax.bar_label(Physics, Physics)
ax.bar_label(Computer,Computer)

ax.set_xticks(ticks = [0,1])
ax.set_xticklabels(["Billy", "Mary"])
# ******************************


fig.savefig('A11.png')
