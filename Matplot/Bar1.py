import matplotlib.pyplot as plt
import numpy as np

# arranging + creating data
col_count = 3
bar_width = .1

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

# Putting data into chart
k1 = plt.bar(index, korea_scores, bar_width, label="Korea", alpha=.8)
c1 = plt.bar(index + bar_width, canada_scores, bar_width, label="Canada", alpha=.8)
ch1 = plt.bar(index + bar_width*2, china_scores, bar_width, label="China", alpha=.8)
f1 = plt.bar(index + bar_width*3, china_scores, bar_width, label="France", alpha=.8)

# Showing graph
plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test Scores by Country")

plt.xticks(index + .3/2, ("Mathematics", "Reading", "Science"))
plt.legend()
plt.grid(True)

plt.show()
