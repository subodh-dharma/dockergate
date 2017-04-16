import os
import json
import hashlib

rawlibc = ''
callq_exc = set()


with open('./data/libc_full.json','r') as libcjson:
 rawlibc = eval(libcjson.read())


def calculate_syscalls(templibc):
 for key in templibc:
  callq_len = len(templibc[key]["callqs"])
  if callq_len > 0:
   #print key, '$$$$$$'
   for index in range(0, callq_len):
    try:
     callq_func = templibc[key]["callqs"][index]
     templibc[key]["syscalls"] = templibc[key]["syscalls"] + templibc[callq_func]["syscalls"]
    except:
     callq_exc.add(callq_func)
 
  index = 0
  callq_l = callq_len
  while index < callq_l:
   callq_func = templibc[key]["callqs"][index]
   #print callq_func, '**********'
   try:
    if len(templibc[callq_func]["callqs"]) == 0:
     templibc[key]["callqs"].remove(callq_func)
     callq_l = callq_l - 1
    index = index + 1
   except:
    index = index + 1 

 return templibc

before_pass = '1'
after_pass = '2'
templibc = rawlibc
count = 0

# check the return value of haslib
while before_pass!=after_pass:
 before_pass = hashlib.md5(str(templibc))
 templibc = calculate_syscalls(templibc)
 after_pass = hashlib.md5(str(templibc))
 print before_pass, '@@', after_pass
 count = count + 1
 print "Pass :", count 


#print rawlibc
#jsonfile = open('./data/libc_out.json', 'w+')
#jsonfile.write(str(rawlibc))
#jsonfile.close() 

#print callq_exc
