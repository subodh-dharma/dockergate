import os
import json

rawlibc = ''
callq_exc = set()


with open('./data/libc_full.json','r') as libcjson:
 rawlibc = eval(libcjson.read())


for key in rawlibc:
 callq_len = len(rawlibc[key]["callqs"])
 if callq_len > 0:
  #print key, '$$$$$$'
  for index in range(0, callq_len):
   try:
    callq_func = rawlibc[key]["callqs"][index]
    rawlibc[key]["syscalls"] = rawlibc[key]["syscalls"] + rawlibc[callq_func]["syscalls"]
   except:
    callq_exc.add(callq_func)
 
 index = 0
 callq_l = callq_len
 while index < callq_l:
   callq_func = rawlibc[key]["callqs"][index]
   #print callq_func, '**********'
   try:
    if len(rawlibc[callq_func]["callqs"]) == 0:
     rawlibc[key]["callqs"].remove(callq_func)
     callq_l = callq_l - 1
    index = index + 1
   except:
    index = index + 1 


#print rawlibc
jsonfile = open('./data/libc_out.json', 'w+')
jsonfile.write(str(rawlibc))
jsonfile.close() 

print callq_exc
