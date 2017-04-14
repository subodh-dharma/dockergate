import os
import json

rawlibc = ''
callq_exc = set()


with open('./data/libc_f.json','r') as libcjson:
 rawlibc = eval(libcjson.read())


for key in rawlibc:
 if len(rawlibc[key]["callqs"]) > 0:
  #print 'do something'
  for index in range(0, len(rawlibc[key]["callqs"])):
   try:
    f_callq = rawlibc[key]["callqs"][index]
    print f_callq
    if len(rawlibc[f_callq]["callqs"]) > 0:
     continue
    else: 
     rawlibc[key]["syscalls"] = rawlibc[key]["syscalls"] + rawlibc[f_callq]["syscalls"]
     rawlibc[key]["callqs"].remove(f_callq)
   except:
    #print 'Function not found in SO', f_callq
    callq_exc.add(f_callq)
    
 else:
  print 'do nothing'


#print rawlibc
jsonfile = open('./data/libc_out.json', 'w+')
jsonfile.write(str(rawlibc))
jsonfile.close() 

print callq_exc
