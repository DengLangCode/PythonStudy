# encoding:utf-8
#python文件处理
import os
if __name__ == "__main__":
    #创建文件夹
    if not os.path.exists("testdir"):
        os.mkdir("testdir")
    """
    open函数，python中的文件操作
    有四种打开文件的不同方法（模式）：
    "r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则报错。
    "a" - 追加 - 打开供追加的文件，如果不存在则创建该文件。
    "w" - 写入 - 打开文件进行写入，如果文件不存在则创建该文件。
    "x" - 创建 - 创建指定的文件，如果文件存在则返回错误。
    此外，您可以指定文件是应该作为二进制还是文本模式进行处理。

    "t" - 文本 - 默认值。文本模式。
    "b" - 二进制 - 二进制模式（例如图像）。
    """
    file = open("testdir\\testfile.txt","at")
    file.write("这是一个测试文件，文件创建在python项目下的文件夹\n创建人：bug不会飞\n")
    file.close()
    file = open("testdir\\testfile.txt","rt")
    info = file.read()
    print("read:\n")
    print(info)
    file.close()
    file = open("testdir\\testfile.txt","rt")
    print("readline:\n")
    print(file.readline())
    file.close()
    pass