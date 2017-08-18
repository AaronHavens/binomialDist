import numpy as np
import matplotlib.pylab as plt
import random as r


states = [0]

iters = 20
step = 1
step_extend = 10
for k in range(iters):
	states_new = []
	for i in range(len(states)):
		if(r.random() > .5):
			states_new.append(states[i]+step_extend)
			states_new.append(states[i]-step_extend)
		else:
			states_new.append(states[i]+step)
			states_new.append(states[i]-step)
	states = states_new

state_counts = [0]*iters*step_extend*2
probs = []

print(len(state_counts))

for i in range(len(states)):
	state_counts[states[i]+k*step_extend-1] += 1
for i in range(len(state_counts)):
	if(state_counts[i] > 0):
		probs.append(state_counts[i])

for i in range(len(probs)):
	probs[i] = float(probs[i]) / float(len(states))
lows =[]
for i in range(len(probs)):
	if(probs[i] < .01):
		lows.append(probs[i])
plt.plot(probs)
plt.show()