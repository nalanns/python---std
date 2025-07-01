import numpy as np
import matplotlib.pyplot as plt

nationalities = ["american", "german", "french", "other"]
students = [60, 23, 21, 34]
explode = [0.2,0,0.1,0]

pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)

plt.pie(students, labels=nationalities, autopct="%.2f%%", shadow=True, startangle=90, counterclock=False)
plt.title("Nationalities")
plt.show()



