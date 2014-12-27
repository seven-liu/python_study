#encoding:utf-8

import codecs
import locale
import sys

text=u'pi: dx'

locale.setlocale(locale.LC_ALL,'')
lang,encoding=locale.getdefaultlocale()
print 'Locale encoding :',encoding
sys.out=codecs.getwriter(encoding)(sys.stdout)

print 'With wrapped stdout:',text
