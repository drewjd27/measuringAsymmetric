import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# TAMPILKAN GRAFIK DISTRIBUSI DATA
jlh_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])
plt.hist(jlh_kucing, bins=4)
plt.show()

# HITUNG SKEWNESS DATA
jlh_kucing_series = pd.Series(jlh_kucing)
print(jlh_kucing_series.skew())
