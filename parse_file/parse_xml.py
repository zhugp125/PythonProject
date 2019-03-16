#!/usr/bin/env python3
# _*_ coding=utf-8 _*_

from xml.etree.ElementTree import parse
from xml.etree.ElementTree import iterparse

doc = parse('rss.xml')
for item in doc.iterfind('channel/item'):
    print(item.findtext('title'))
    print(item.findtext('pubDate'))
    print(item.findtext('link'))
    print()

ele = doc.find('channel/link')
print('tag =', ele.tag)
print('text =', ele.text)

data = iterparse('rss.xml', ('start', 'end'))
for event, ele in data:
    print(ele.tag, '>', ele.text)

# 解析xml也可以考虑lxml
# from lxml.etree import parse

print('############################')

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring
from xml.etree.ElementTree import ElementTree

def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem

s = {'name': 'ALiBaBa', 'count': 100, 'price': 234.56}
elem = dict_to_xml('stock', s)

print(tostring(elem))

document = ElementTree(element=elem)
document.write('stocks.xml', xml_declaration=True, encoding='utf-8')