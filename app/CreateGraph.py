import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

with open('results') as f:
   lines = [line.rstrip('\n') for line in f]
x =[]
y = []
for i in range(0,len(lines),2):
  x.append(lines[i])
  y.append(lines[i+1])
y_pos = np.arange(len(x))
plt.bar(y_pos,y,align='center',alpha=.5)
plt.xticks(y_pos,x)
plt.ylabel('Frequency')
plt.xlabel('Guess')
plt.title('Number of incidents per guess')
plt.savefig('plot.png')
exit()

