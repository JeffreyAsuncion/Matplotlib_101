import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
values = [1, 4, 2]

plt.figure(figsize=(10,4))

bars = plt.bar(labels, values)

patterns = ['/','o','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')


plt.show()

