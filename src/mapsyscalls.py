import subprocess
import sys
import json

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
    if sys_num.startswith('sys_'):
     sys_num = sys_num.strip('sys_')
    syscalls.add(sys_num)
  except:
   try:
    for sys_num in (libc['__' + value]["syscalls"]):
     if sys_num.startswith('sys_'):
      sys_num = sys_num.strip('sys_')
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

