#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#import library to do http requests:
import urllib2
 #import easy to use xml parser called minidom:
from xml.dom.minidom import parseString
#all these imports are standard on most modern python implementations
 
file = urllib2.urlopen('https://www.facebook.com/feeds/notifications.php?id=750373691&viewer=750373691&key=AWjEZzYVFFPQo2et&format=rss20')
data = file.read()
dom = parseString(data)


#afficher les 7 dernieres notifs FB

xmlTag1 = dom.getElementsByTagName('title')[1].toxml()
xmlData1=xmlTag1.replace('<title><![CDATA[','').replace(']]></title>','').replace('','').replace('','')
xmlTag2 = dom.getElementsByTagName('title')[2].toxml()
xmlData2=xmlTag2.replace('<title><![CDATA[','').replace(']]></title>','')
xmlTag3 = dom.getElementsByTagName('title')[3].toxml()
xmlData3=xmlTag3.replace('<title><![CDATA[','').replace(']]></title>','')
xmlTag4 = dom.getElementsByTagName('title')[4].toxml()
xmlData4=xmlTag4.replace('<title><![CDATA[','').replace(']]></title>','')
xmlTag5 = dom.getElementsByTagName('title')[5].toxml()
xmlData5=xmlTag5.replace('<title><![CDATA[','').replace(']]></title>','')
xmlTag6 = dom.getElementsByTagName('title')[6].toxml()
xmlData6=xmlTag6.replace('<title><![CDATA[','').replace(']]></title>','')
xmlTag7 = dom.getElementsByTagName('title')[7].toxml()
xmlData7=xmlTag7.replace('<title><![CDATA[','').replace(']]></title>','')


print xmlData1
print xmlData2
print xmlData3
print xmlData4
print xmlData5
print xmlData6
print xmlData7

file.close()
