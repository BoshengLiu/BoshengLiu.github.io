
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy import stats, integrate
from sklearn.datasets import load_iris

''' 整体布局风格设置    '''

# def sinplot(flip=1):
#     x = np.linspace(0, 14, 100)
#     for i in range(1,7):
#         plt.plot(x, np.sin(x+i*.5)*(7-i)*flip)
#
# sns.set()
# # sns.set_style("whitegrid")
# # sns.set_style("ticks")
# # sns.despine(offset=10,left=True,bottom=True,right=False,top=False)
# # sns.set_context("paper")
# # sns.set_context("talk")
# # sns.set("poster")
# sns.set("notebook",font_scale=3,rc={"lines.linewidth":2})
#
#
# sinplot()
# plt.show()



''' 调色板 '''

#离散型
# data = np.random.normal(size=(20,8)) + np.arange(8)/2
# current_pattern = sns.color_palette('hls',8)
# # sns.palplot(current_pattern)
# sns.palplot(sns.hls_palette(8,l=5,s=9))
# sns.palplot(data=data,palette=current_pattern)
# sns.palplot(sns.color_palette("Paired",10))


#连续型
# sns.palplot(sns.color_palette("Blues"))
# sns.palplot(sns.color_palette("BuGn_r"))
# sns.palplot(sns.color_palette("cubehelix",8))
#
# sns.palplot(sns.cubehelix_palette(8, start=0.5, rot= -0.75))
#
# sns.palplot(sns.light_palette("green"))
# sns.palplot(sns.dark_palette("purple"))
#
# plt.show()



''' 单变量分析绘图 '''

# x1 = np.random.normal(size=100)
# sns.set()
# sns.distplot(x1,bins=20,kde=False)

# x2 = np.random.gamma(6,size=200)
# sns.set()
# sns.distplot(x2, kde=False, fit=stats.gamma)

# mean, cov = [0,1], ([1,.5],[.5,1])
# data = np.random.multivariate_normal(mean, cov,200)
# df = pd.DataFrame(data, columns=["x","y"])
# sns.set()
# sns.jointplot(x="x",y="y",data=df)
#
# print(df)

# x,y = np.random.multivariate_normal(mean, cov, 5000).T
# with sns.axes_style("white"):
#     sns.jointplot(x=x, y=y, kind="hex", color="k")

# iris = sns.load_dataset('iris')
# sns.set()
# sns.pairplot(iris)

# plt.show()



''' 回归分析绘图  '''

# sns.set(color_codes=True)
# np.random.seed(sum(map(ord, "regression")))
# tips = sns.load_dataset("tips")
#
# # sns.regplot(x="total_bill", y="tip", data=tips)
# sns.regplot(x="size", y="tip", data=tips, x_jitter=0.05)
#
# print(tips.head())
#
# plt.show()



''' 多变量分析绘图 '''
#
# sns.set(style="whitegrid", color_codes=True)
#
# np.random.seed(sum(map(ord, "categorical")))
# titanic = sns.load_dataset("titanic")
# tips = sns.load_dataset("tips")
# iris = sns.load_dataset("iris")
#
# # sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)
# # sns.swarmplot(x="day", y="total_bill", hue="sex", data=tips)
# # sns.boxplot(x="day", y="total_bill", data=tips)
# # sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
#
# # sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
# # sns.swarmplot(x="day", y="total_bill", data=tips, color='w', alpha = 0.5)
# # sns.barplot(x="sex", y="survived", hue="class", data=titanic)
# # sns.pointplot(x="sex", y="survived", hue="class", data=titanic)
#
# # sns.pointplot(x="class", y="survived", hue="sex", data=titanic, palette={"male":'g',"female":"m"}, markers=["^","o"], linestyles=["-","--"])
# # sns.boxplot(data=iris, orient='h')
#
# sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar")

# plt.show()



''' Facetgrid '''

tips = sns.load_dataset("tips")

# g = sns.FacetGrid(tips,col="time")
# g.map(plt.hist, "tip")

# g = sns.FacetGrid(tips,col="sex", hue = smoker")
# g.map(plt.scatter, "total_bill", "tip", alpha = 0.7)
# g.add_legend()

# g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
# g.map(sns.regplot, "size", "total_bill", color="0.1", fit_reg = True, x_jitter = 1)

# g = sns.FacetGrid(tips, col="day", size=4, aspect=0.5)
# g.map(sns.barplot, "sex", "total_bill")

# pal = dict(Lunch = "seagreen", Dinner = "gray")
# g = sns.FacetGrid(tips, hue="time", palette=pal, size=5)
# g.map(plt.scatter, "total_bill", "tip", s=50, alpha = 0.7, linewidth = 0.5, edgecolor = "white")
# g.add_legend()

# with sns.axes_style("white"):
#     g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, size=2.5)
# g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=0.5)
# g.set_axis_labels("Total_bill (US Dollars)", "Tip")
# g.set(xticks=[10,30,50], yticks=[2,6,10])
# g.fig.subplots_adjust(wspace=0.02, hspace=0.02)

# iris = sns.load_dataset("iris")
# # g = sns.PairGrid(iris)
# # g.map(plt.scatter)
#
# # g = sns.PairGrid(iris)
# # g.map_diag(plt.hist)
# # g.map_offdiag(plt.scatter)
#
# # g = sns.PairGrid(iris, hue="species")
# # g.map_diag(plt.hist)
# # g.map_offdiag(plt.scatter)
# # g.add_legend()
#
# # g = sns.PairGrid(iris, vars=["sepal_length","sepal_width"], hue="species")
# # g.map(plt.scatter)
#
# g = sns.PairGrid(tips, hue="size", palette="GnBu_d")
# g.map(plt.scatter, s=50, edgecolor="white")
# g.add_legend()
#
# plt.show()



''' 热度图绘制   '''

# uniform_data = np.random.rand(3, 3)
# print(uniform_data)
# heatmap = sns.heatmap(uniform_data, vmin=0.2, vmax=0.5, center=0)

flights = sns.load_dataset("flights")
flights = flights.pivot("month","year","passengers")
ax = sns.heatmap(flights, annot=True, fmt="d", linewidths=0.5)
# ax = sns.heatmap(flights, cmap="YlGnBu")

plt.show()