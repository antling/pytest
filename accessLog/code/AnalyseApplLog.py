import os
import re
import easygui as g
import datetime

# path = r"d:/work/antling"
# files = os.listdir(path)
#
# for file in files:
#     if not os.path.isdir(file):
#         print("antling path = ", path, " file = " , file)
#         f = open(path + "/" + file)
#         iter_f = iter(f)
#         print(iter_f)
#         for line in iter_f:
#             if (line.find("error") > -1) or (line.find("fatal") > -1) or (line.find("exception") > -1) or (
#                     line.find("exception1") > -1):
#                 result = re.findall(r'error|fatal|exception1|exception', line)
#                 print(line)
#                 target.writelines(line)
#
# target.close()
# now_time = datetime.datetime.now()
# print(now_time, "Analysis log completed.")


def search_file(start_dir):
    img_list = []
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        img_prop = os.path.splitext(each_file)

        fl1 = os.getcwd() + os.sep + each_file

        if os.path.isfile(fl1):
            img_list.append(fl1)
            print("file = ", fl1)

        if os.path.isdir(each_file):
            print("run here")
            img_list.append(search_file(each_file))
            os.chdir(os.pardir)

    return img_list


file_list = search_file(r'D:\work\ziplog-0808191948')

print("file count = ", len(file_list))

target = open(r'c:/wuda/trace.log', 'w')

for file in file_list:
    f = open(file)
    iter_f = iter(f)
    print(iter_f)
    for line in iter_f:
        if (line.find("error") > -1) or (line.find("fatal") > -1) or (line.find("exception") > -1) or (
                line.find("exception") > -1):
            result = re.findall(r'error|fatal|exception|exception', line)
            target.writelines(line)

target.close()
