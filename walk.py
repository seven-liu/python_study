import os
def walk_dir(dir):
    list1=[]
    for root, dirs, files in os.walk(dir):
        for name in files:
            file=os.path.join(root,name)
            list1.append(file)
        for name in dirs:
            file=(os.path.join(root,name))
            list1.append(file)
    return list1
dir='d:\\test'
DIR=walk_dir(dir)
for file in DIR:
    print file
