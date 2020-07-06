# matplotlib使用

* 折线图

        unrate = pandas.read_csv("UNRATE.csv")
        unrate["DATE"] = pandas.to_datetime(unrate["DATE"])     # 转换时间格式
        
        first_year = unrate[0:12]
        plt.plot(first_year['DATE'],first_year['VALUE'])        # 将数据导入图表
        
        plt.xticks(rotation=45)                                 # x轴数据旋转45°
        plt.yticks(rotation=45)                                 # y轴数据旋转45°
        
        plt.xlabel('Month')                                     # x轴添加数据
        plt.ylabel('Unemployment Rate')                         # y轴添加数据
        plt.title('Monthly Unemployment Trends, 1948')          # 添加标题
        
        plt.show()                                              # 显示图形
        
* 子图操作

        fig = plt.figure(figsize=(6,6))          # 生成子图,figsize指图的大小
        fig.add_subplot(2,2,2)                   # 生成2x2的子图，图形位置为2，排序规则从左到右，从上到下
        
        plt.plot(unrate[0:12]["Month"], unrate[0:12]["VALUE"], c = 'red')
        plt.plot(unrate[12:24]["Month"], unrate[12:24]["VALUE"], c = 'blue')
        # 在一个图形中生成两条折线
    

* 条形图与散点图

        bar_heights = films.loc[0,cols].values     # 条形柱高度
        bar_position = np.arange(5) + 0.75         # 条形柱位置
        fig,ax = plt.subplots()                    # 生成条形柱状图
                

* 柱形图与盒图

        ax.hist(films["Fandango_Ratingvalue"], range=(4,5), bins=20)
        # 生成柱形图，range指起始区间，bins指个数
        ax.set_ylim(0,50)       #设置y轴的范围
        
        ax.boxplot(films["RT_user_norm"])               # 生成盒图
        ax.set_xticklabels(["Rotten Tomatoes"])         # 设置x轴名称
        
        
* 更多细节操作

        ax.tick_params(bottom='off', top='off', left='off', right='off')
        # 去掉图形的小突出      
        cb_dark_blue = (0/255,107/255,164/255)      # 定义新的颜色
        fig = plt.figure(figsize=(18,3))            # 可以设置figsize使得图形便于对比观察
        ax.plot(linewith=5)                         # 设置线的宽度

        # 在某个图的线上添加文字
        if sp == 0:
            ax.text(2002,8,'Women')
            ax.text(2005,87,'men')
        