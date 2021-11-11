import os
import re
import easygui as g
import datetime

def search_file(start_dir):
    img_list = []
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        fl = os.getcwd() + os.sep + each_file

        if os.path.isfile(fl):
            img_list.append(fl)
        elif os.path.isdir(fl):
            img_list.extend(search_file(fl))
            os.chdir(os.pardir)
    return img_list

file_list = search_file(r'D:\work\appserver7_0808')
target = open(r'd:\work\trace.log', 'w')

for file in file_list:
    print("File name = ", file)
    f = open(file, encoding='utf8')
    for line in f:
        if (line.find("error") > -1) or (line.find("fatal") > -1) or (line.find("exception") > -1):
            target.writelines(line)

target.close()
now_time = datetime.datetime.now()
print(now_time, "Analysis log has been completed.")