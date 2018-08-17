# coding:utf8
import os

def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1]=='.trans':
            list_name.append(file_path)
    return list_name

def listdir2(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1]=='.stats':
            list_name.append(file_path)
    return list_name


def spilts(list_name):
    file_list = []
    length = len(list_name)
    for i in range(length):
        a = list_name[i].split('/')
        file_list.append(a[len(a)-1])
    return file_list


def create_file(name, msg):
    full_name = name + ".txt"
    file = open(full_name, "w")
    file.write(msg)
    print 'Generate success'


