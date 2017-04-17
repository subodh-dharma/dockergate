import os
import json


rawlibc = ''
callq_exc = set()


with open('./data/libc_full.json','r') as libcjson:
 rawlibc = eval(libcjson.read())


def calculate_syscalls(templibc):
 for key in templibc:
  callq_len = len(templibc[key]["callqs"])
  if callq_len > 0:
   for index in range(0, callq_len):
    try:
     callq_func = templibc[key]["callqs"][index]
     templibc[key]["syscalls"] = mergelist(templibc[key]["syscalls"],templibc[callq_func]["syscalls"])
    except:
     callq_exc.add(callq_func)
 
  index = 0
  callq_l = callq_len
  while index < callq_l:
   callq_func = templibc[key]["callqs"][index]
   try:
    if len(templibc[callq_func]["callqs"]) == 0:
     templibc[key]["callqs"].remove(callq_func)
     callq_l = callq_l - 1
    index = index + 1
   except:
    index = index + 1 

 return templibc


def mergelist(list1, list2):
 result = list1
 for val in list2:
  if val in list1:
   continue
  else:
   result.append(val)

 return result
  

templibc = rawlibc
count = 0

# check the return value of haslib
while count < 5:
 templibc = calculate_syscalls(templibc)
 count = count + 1
 print "Pass :", count 


#print rawlibc
jsonfile = open('./data/libc_out.json', 'w+')
jsonfile.write(str(rawlibc))
jsonfile.close() 

#print callq_exc
excfile = open('./data/libc_pass_exc.txt', 'w+')
excfile.write(str(callq_exc))
excfile.close() 
