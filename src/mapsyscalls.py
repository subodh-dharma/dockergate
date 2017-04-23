import subprocess
import sys
import json
import os

def copy_new_mapping(filename):
 f = open(filename,'r')
 index = open('index_tmp','w')
 out = open('output_mapping_tmp','w')
 in_index = False
 in_json = False
 for line in f:
  if 'START INDEX' in line:
   in_index = True
   continue
  if 'END INDEX' in line:
   in_index = False
  if in_index:
   index.write(line.strip() + '\n')
  if 'START JSON' in line:
   in_json = True
   continue
  if in_json:
   out.write(line)
 index.close()
 out.close()
 if os.stat('index_tmp').st_size>0 and os.stat('output_mapping_tmp').st_size>0:
  os.rename('index_tmp','./src/data/index')
  os.rename('output_mapping_tmp','./src/data/output_mapping')
  
def map_nm_2_sys(filename):

 file_name = filename
 #file_name = sys.argv[1]

 #output = subprocess.check_output(['nm','-D',file_name])
 #output_list = output.splitlines()

 output_list = ''
 
 with open(file_name, 'r') as output:
  output_list = output.readlines()

 for value in output_list:
  if 'U' not in value:
   #print value
   output_list.remove(value)
 #print '***'   

 for index in range(0, len(output_list)):
  if 'U' in output_list[index]:
   output_list[index] = output_list[index].split('U')[1].strip()

 libc = ''

 with open('./src/data/output_mapping', 'r') as libcfile:
  libc = eval(libcfile.read())

 syscalls = set()
 exceptions = set()
 for value in output_list:
  try:
   for sys_num in (libc[value]["syscalls"]):
    syscalls.add(sys_num)
  except:
   try:
    for sys_num in (libc['__' + value]["syscalls"]):
     syscalls.add(sys_num)
   except:
     try:
      for sys_num in (libc['_IO_' + value]["syscalls"]):
       syscalls.add(sys_num)
     except:
      exceptions.add(value)
    #print 'Doesn\'t exist in lib :', value
 writePolicyFile(syscalls)


def writePolicyFile(syscalls):
 
 policy = {}
 policy["defaultAction"] = "SCMP_ACT_ERRNO"
 policy["syscalls"] = []
 for syscall in syscalls:
  s = {}
  s['name'] = syscall
  s["action"] = "SCMP_ACT_ALLOW"
  s["args"] = []
  policy["syscalls"].append(s)
 
 policyjson = open('./policy_generated.json', 'w+')
 policyjson.write(json.dumps(policy))
 policyjson.close()

