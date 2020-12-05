import geopandas
import matplotlib.pyplot as plt


world = geopandas.read_file("D:\数据\林shp 2000 (1)\高淳二调-刘杉shp\高淳shp\村.shp")
world.plot()
plt.show()