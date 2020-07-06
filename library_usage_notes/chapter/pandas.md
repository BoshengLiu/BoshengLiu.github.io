# pandas 使用教程
* 文件读取

        pandas.read_csv("pandas.csv")       # 读取.csv文件，更多参考官方文档
        
        file_info.head(3)                   # 读取前3行，默认为5
        file_info.tail(3)                   # 读取后3行，默认为5
        file_info.colsums                   # 查看列的数据
        file_info.shape                     # 查看行信息
        file_info.culsums.tolist()          # 查看列的列信息
        file_info.loc[0]                    # 定位第一列数据
        file_info.loc[3:8]                  # 查找第4-8行的数据
        file_info["Nodted"]                 # 查找列为Nodted的数据

     

* 数据处理

        file_info["Nodted"].max()                           # 查找每列的最大值
        
        file_info.sort_values("Teach(mg)",inplace=True)     # 排序该列，默认正序
        
        file_info.sort_values("Teach(mg)", inplace=True, ascending=False)
        # 给该列排序，降序操作
        
        A.reset_index(drop=True)    # 对排序后的列生成新的索引
        
        file_info.isnull("age")     # 判断该列的值是否有空
        
        file_info["Age"].mean()     # 求该列的均值
        
        file_info.pivot_table(index="Place",values="Survived",aggfunc=numpy.mean)   
        #对该列进行数据统计，求均值，aggfunc可以不写，默认求均值，values的值可以为多个用[]
        
        file_info.dropna(axis=0,subset=["Age","Sex"])       # 去掉该列有缺失值的部分
        file_info.loc[85,"Age"]                             # 定位该位置的样本值        
        
        file_info.apply(vlaue_text)                         # 调用自定义函数value_text

* series结构

        serices.index.tolist()                              # 将目录列表化
        serices_new.reindex(new_index)                      # 重新排列目录
        # 注：其用法和numpy一样，可以混合使用
