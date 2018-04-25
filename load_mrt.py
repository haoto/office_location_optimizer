# -*- coding: utf8 -*-
import re
import urllib.request

fp = urllib.request.urlopen('https://web.metro.taipei/c/selectstation2010.asp')
txt = fp.read().decode('utf8')
p = re.compile('>[A-Z0-9]{2,6} .{2,10}<\/option>')
p2 = re.compile('<\/option>')
p3 = re.compile('.* ')
stations = [p2.sub('站, Taipei, Taiwan', p3.sub('捷運', m)) for m in p.findall(txt)]
stations_unique = []
[stations_unique.append(s) for s in stations if s not in stations_unique]
open('destinations', 'w').write('\n'.join(stations_unique))
