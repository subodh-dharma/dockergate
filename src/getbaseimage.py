import os
import json
import operator

files = os.listdir('./downloads1')
baseimages = {}
for f in files:
 fo = open('./downloads1/'+f)
 line = fo.readline()

 while line:
  if 'FROM' in line:
   print line
   if len(line.split(' ')) != 2:
    break
   image_name = line.split(' ', 1)[1].rstrip().lstrip()
   # general image names
   image_name = image_name.split(':',1)[0]
   if baseimages.has_key(image_name):
    val = baseimages.get(image_name)
    baseimages[image_name] = val + 1
   else:
    baseimages[image_name] = 1
   #print image_name
   break
  line = fo.readline()
 
 fo.close()

print json.dumps(baseimages, indent=2)
