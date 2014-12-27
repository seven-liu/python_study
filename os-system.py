#coding=utf-8

import os
import time


if os.name=="nt":
    command="dir"
else:
    command="ls |wc -l"


os.system(command)

