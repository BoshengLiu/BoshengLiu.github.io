import os
from string import digits


class BatchRename():

    def __init__(self):
        # 文件存放目录
        self.spath = 'test/'
        self.dpash = 'Sensetime-rename/'
        self.endpash = 'Sensetime-end/'


    def rename(self):
        filelist = os.listdir(self.spath)
        rename_fileList = os.listdir(self.dpash)
        total_num = len(filelist)
        i = 0
        num = 0
        for item in filelist:
            if item.endswith('.jpg'):
                if len(item.split("-")) == 2:
                    src = os.path.join(os.path.abspath(self.spath), item)
                    dst = os.path.join(os.path.abspath(self.dpash), item.split("-")[0] + '.jpg')
                    try:
                        print(src)
                        os.rename(src, dst)
                        print('converting %s to %s ...' % (item, item.split("-")[0] + '.jpg'))
                        i = i + 1
                    except Exception as e:
                        if e.args[0] == 17:
                            print("####", item)
                            dst = os.path.join(os.path.abspath(self.dpash), item.split("-")[0] + str(num) + '.jpg')
                            os.rename(src, dst)
                            num += 1
                            # continue
                else:
                    print(item)
                    print(len(item.split("-")))
        print('total %d to rename & converted %d pngs' % (total_num, i))

        # 处理名字重名   重名数量统计入字典


    def CheckDuplicateDname(self):
        i = 0
        name_dict = {}
        rename_fileList = os.listdir(self.dpash)
        for item in rename_fileList:
            name = item.translate(str.maketrans('', '', digits)).split(".")[0]
            src = os.path.join(os.path.abspath(self.dpash), item)
            dst = os.path.join(os.path.abspath(self.endpash), name + '.jpg')
            if name not in name_dict.keys():
                print(item, item not in name_dict)
                os.rename(src, dst)
                name_dict[name] = 1
                i += 1

            else:
                try:
                    dst = os.path.join(os.path.abspath(self.endpash), name + str(name_dict[name]) + '.jpg')
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (item, item.split("-")[0] + '.jpg'))
                    i = i + 1
                    name_dict[name] += 1
                except Exception as e:
                    print(item)

                    # contin
        print(name_dict)
        print("total:", i)
        print(sum(name_dict.values()))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
    demo.CheckDuplicateDname()
