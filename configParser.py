#encoding:utf-8

import ConfigParser
import sys

config=ConfigParser.ConfigParser()

config.add_section("book")
config.set("book","title","the python standard library")
config.set("book","author","fredrik lundh")

config.add_section("ematter")
config.set("ematter","pages",250)

config.write(sys.stdout)


