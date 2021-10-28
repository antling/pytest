import os
import re
import datetime

path = r"c:/wuda/ziplog-0808191948"
target = open(r'c:/wuda/result.log', 'w')
files = os.listdir(path)

for file in files:
    if not os.path.isdir(file):
        f = open(path + "/" + file)
        iter_f = iter(f)
        print(iter_f)
        for line in iter_f:
            if (line.find("error") > -1) or (line.find("fatal") > -1) or (line.find("exception") > -1) or (
                    line.find("exception1") > -1):
                result = re.findall(r'error|fatal|exception1|exception', line)
                print(line)
                target.writelines(line)

target.close()
now_time = datetime.datetime.now()
print(now_time, "Analysis log completed.")
