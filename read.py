import os

res = []
for root, subdirs, files in os.walk("/home/crabron/Документы/dir/main"):
    for i in files:
        if i.endswith(".py"):
            dir_list = [a for a in root.split("/")]
            res.append("/".join(dir_list[5:]))
            break
res.sort()
with open('/home/crabron/Документы/dir/your_file.txt', 'w') as f:
    for item in res:
        f.write("%s\n" % item)


