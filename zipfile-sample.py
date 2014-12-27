#encoding:utf-8

import zipfile

file=zipfile.ZipFile("d:\download\records_deeb928479c311e49acec81f66b811c1.zip","r")
for name in file.namelist():
    print namelist

for info in file.infolist():
    print info.filename,info.date_time,info.file_size


