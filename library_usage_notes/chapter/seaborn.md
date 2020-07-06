# seabon教程

* 整体布局风格设置

        seaborn.set()                               # 默认背景设置
        sns.set_style("whitegrid")                  # 背景设置成白色，还有dark,darkgrid,white
        sns.set_style("ticks")                      # 给坐标值加上线段
        sns.despine(offset=100)                     # 将图形远离轴线100单位
        sns.despine(left=True)                      # 隐藏左轴线，还有top,bottom,right
        
        sns.set("notebook",font_scale=2.5,rc={"lines.linewidth":2})        
        # 设置格子的大小，还可以为poster,paper,notebook;设置字体大小以及线条粗细

* 调色板-离散型

        sns.color_palette('hls',12)                         # 调色板设置,平均分成12种颜色
        sns.palplot(current_pattern)                        # 打印调色板        
        sns.boxplot(data=data,palette=sns.color_palette('hls',12))          #设置盒图的数据以及颜色       
        sns.palplot(sns.hls_palette(8,l=5,s=9))             # 设置颜色8种，亮度以及饱和度        
        sns.palplot(sns.color_palette("Paired",10))         # 设置对比色，每两个一对进行对比，共10种颜色        

* 调色板-连续型

        sns.palplot(sns.color_palette("Blues"))             # 连续型颜色由浅到深
        sns.palplot(sns.color_palette("BuGn_r"))            # 连续型颜色由深到浅
        
        sns.palplot(sns.color_palette("cubehelix",8))       # 色调线性变换
        sns.palplot(sns.cubehelix_palette(8, start=0.5, rot= -0.75))
        
        sns.palplot(sns.light_palette("green"))             # 绿色由浅到深
        sns.palplot(sns.dark_palette("purple"))             # 紫色由深到浅,加reverse反转

* 单变量分析绘图

        from scipy import stats, integrate              # 要导入这个库
        x2 = np.random.gamma(6,size=200)
        sns.set() 
        sns.distplot(x2, kde=False, fit=stats.gamma)    # 设置fit可以查看数据的分布情况，还可以设置bins
        
        mean, cov = [0,1], ([1,.5],[.5,1])
        data = np.random.multivariate_normal(mean, cov,200)
        df = pd.DataFrame(data, columns=["x","y"])      # 根据均值和协方差生成数据，观测两个变量之间的关系
        sns.jointplot(x="x",y="y",data=df)              # 将数据导入生成散点图，数据少时可以使用这个
        
        # 当数据量比较大时，可以通过这种方式查看数据的分布，颜色越深分布越多
        x,y = np.random.multivariate_normal(mean, cov, 5000).T
        with sns.axes_style("white"):
            sns.jointplot(x=x, y=y, kind="hex", color="k")
            
        from sklearn.datasets import load_iris          # 要导入这个机器学习包
        iris = sns.load_dataset('iris')
        sns.pairplot(iris)                              # 当有多个数据类型时,可以将数据中两两关系显示出来

* 回归分析绘图 

        sns.set(color_codes=True)
        np.random.seed(sum(map(ord, "regression")))        
        tips = sns.load_dataset("tips")                         # 调用自带的数据集
        
        sns.regplot(x="total_bill", y="tip", data=tips)         # 调用回归函数
        
        sns.regplot(x="size", y="tip", data=tips, x_jitter=0.05)
        # x_jitter设置的是回归函数的偏移
        print(tips.head())

* 多变量分析绘图

        sns.stripplot(x="day", y="total_bill", data=tips, jitter=True) 
        # 设置jitter=True使得数据不重叠
        
        sns.swarmplot(x="day", y="total_bill", data=tips)
        sns.violinplot(x="day", y="total_bill", hue="sex", data=tips, split=True)
        # 小提琴图，设置split可以使得对比更明显
        
        sns.pointplot(x="sex", y="survived", hue="class", data=titanic) 
        # 点图可以更好地描述变化差异
        
        sns.boxplot(data=iris, orient='h')  #盒图，设置为横向
        
        sns.pointplot(x="class", y="survived", hue="sex", data=titanic, 
        palette={"male":'g',"female":"m"}, markers=["^","o"], linestyles=["-","--"])
        # palette设置颜色，markers设置不同的对象用不同的方式表示，linestyles设置线的样式
        
        sns.factorplot(x="day", y="total_bill", hue="smoker", data=tips, kind="bar") 
        # 多层面板分类图，折线图，加个bar为条形图
 
 * Facetgrid 使用
 
        tips = sns.load_dataset("tips")
        g = sns.FacetGrid(tips,col="time")
        g.map(plt.hist, "tip")
        
        g = sns.FacetGrid(tips,col="sex", hue="smoker")
        g.map(plt.scatter, "total_bill", "tip", alpha = 0.7)        # alpha指透明程度
        g.add_legend()
        
        g = sns.FacetGrid(tips, row = "smoker", col = "time", margin_titles = True)
        g.map(sns.regplot, "size", "total_bill", color = "0.1", fit_reg = True, x_jitter = 1)
        # fit_reg指回归线是否表示出来
        
        g = sns.FacetGrid(tips, col="day", size=4, aspect=0.5)      # 图形的大小设置
        g.map(sns.barplot, "sex", "total_bill")
        
        pal = dict(Lunch = "seagreen", Dinner = "gray")
        # 将颜色设置成字典形式
        
        g = sns.FacetGrid(tips, hue="time", palette=pal, size=5) 
        # palette设置颜色
        
        g.map(plt.scatter, "total_bill", "tip", s=50, alpha = 0.7, linewidth = 0.5, edgecolor = "white")
        # s设置的是点的大小，linewidth设置的是线宽，edgecolor设置的是边界颜色
        
        g.add_legend()
        
        with sns.axes_style("white"):
            g = sns.FacetGrid(tips, row="sex", col="smoker", margin_titles=True, size=2.5)
            g.map(plt.scatter, "total_bill", "tip", color="#334488", edgecolor="white", lw=0.5)
            g.set_axis_labels("Total_bill (US Dollars)", "Tip")                 #设置x、y轴的名字
            g.set(xticks=[10,30,50], yticks=[2,6,10])                           #设置x、y轴的的取值范围
            g.fig.subplots_adjust(wspace=0.02, hspace=0.02)                     #设置子图之间的间隔
        
        iris = sns.load_dataset("iris")
        g = sns.PairGrid(iris)
        g.map(plt.scatter)
        
        iris = sns.load_dataset("iris")
        g = sns.PairGrid(iris)
        g.map_diag(plt.hist)
        g.map_offdiag(plt.scatter)          #设置对角线和非对角线的图形
        
        g = sns.PairGrid(iris, vars=["sepal_length","sepal_width"], hue="species")      #var设置指定的对象
        g.map(plt.scatter)
        
        g = sns.PairGrid(tips, hue="size", palette="GnBu_d")
        g.map(plt.scatter, s=50, edgecolor="white")
        g.add_legend()
        
* 热度图绘制

        uniform_data = np.random.rand(3, 3)
        heatmap = sns.heatmap(uniform_data, vmin=0.2, vmax=0.5, center=0)
        # 可以观察数值的变化以及所在区间,可以设置最大最小值，设置值的中心
        
        flights = sns.load_dataset("flights")
        flights = flights.pivot("month","year","passengers")
        ax = sns.heatmap(flights, annot=True, fmt="d", linewidths=0.5, cmap="YlGnBu")
