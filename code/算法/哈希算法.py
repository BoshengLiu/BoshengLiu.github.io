import hashlib


def myHash(input):
    output = input // 10 + input % 2
    return output


def pyMd5(data):
    """ 查看 md5 哈希值 """
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    print("Hash: %s" % md5.hexdigest())


if __name__ == '__main__':
    data1 = "welcome to UK."
    data2 = "welcome to UK!"
    pyMd5(data1)
    pyMd5(data2)
