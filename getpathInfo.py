import os

def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__ == '__main__':
    print('测试的路径是否ok，路径为：', get_Path())