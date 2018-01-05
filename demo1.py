# coding:utf-8
import re
import os

# def recur_fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (recur_fibo(n - 1) + recur_fibo(n - 2))
#
#
# # 获取用户输入
# nterms = int(input("请输入： "))
# # 检查输入的数字是否正确
# if nterms <= 1:
#     print nterms
# else:
#     print("the fibo_list is:")
#     for i in range(nterms):
#         print(recur_fibo(i))

# CONF_PATH = r"C:\Users\DH\Desktop\face\chaxun"
# f = open(CONF_PATH, "r+")
# a = f.read()
# l = re.findall(r'"recordCount":(.*?),', a)
# f.close()
# sum = 0
# for i in l:
#     sum += int(i)
#
# print sum

# FileList = []
# CONF_PATH = r"C:\Users\DH\Desktop\Vehiclecloud_autotest\TEST\03_组织"
# upath = unicode(CONF_PATH, 'utf-8')
# FileNames = os.listdir(upath)
# sum1 = 0
# for i in FileNames:
#     file_path = os.path.join(upath, i)
#     f = open(file_path, 'rb')
#     sum1 += len(f.readlines())
#     f.close()
# print sum1

# dir_path = r'C:\Users\DH\Desktop\Vehiclecloud_autotest\TEST'
# upath = unicode(dir_path, 'utf-8')
# #FileNames = os.listdir(upath)
# print os.path.abspath(upath)
# print os.path.basename(upath)
# print os.path.dirname(upath)
# print os.path.isdir(upath)
# print os.path.join(upath, 'guxw')
# print os.path.normpath(upath)


# 获取某文件夹下所有文件路径，包括子文件下的文件
def catch_files(path=''):
    ret_list = []
    file_names = os.listdir(path)
    for i in file_names:
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path):
            ret_list.append(file_path)
        else:
            second_file_list = catch_files(file_path)
            ret_list += second_file_list
    return ret_list


# 计算所有文件总行数
def sum_file_lines(files_path=[]):
    sum_line = 0
    if files_path:
        for i in files_path:
            f = open(i, 'rb')
            fline = len(f.readlines())
            print i + '\t' + u'该文件行数:' + str(fline)
            sum_line += fline
            f.close()
    return sum_line


if __name__ == '__main__':
    fpath = r'C:\Users\DH\Desktop\Vehiclecloud_autotest\TEST'
    upath = unicode(fpath, 'utf-8')
    flist = catch_files(upath)
    print u'合计文件行数：' + str(sum_file_lines(flist))




