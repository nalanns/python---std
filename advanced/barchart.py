import matplotlib.pyplot as plt
import numpy as np

python = (85, 67, 23, 58)
java = (50, 67, 89, 12)
networking = (60 , 20, 56, 22)
machine_learning = (88, 23, 40, 17)

people = ["bob", "anna", "john", "mark"]

index = np.arange(4)
plt.bar(index, python, width=0.2, label="python")
plt.bar(index + 0.2, java, width=0.2, label="java")
plt.bar(index + 0.4, networking, width=0.2, label="networking")
plt.bar(index + 0.6, machine_learning, width=0.2, label="machine_learning")

plt.title("IT skills")
plt.xlabel("skills")
plt.ylabel("level")
plt.xticks(index + 0.2, people)
plt.legend(loc="upper right")
plt.ylim(0, 120)

plt.show()

