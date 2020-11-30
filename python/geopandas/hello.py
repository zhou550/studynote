import pandas as pd
import geopandas
import matplotlib.pyplot as plt
# %matplotlib inline

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world.plot()
plt.show()