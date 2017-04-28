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
 
 try:
  removeUnknownSyscalls(syscalls)
 except:
  print 'Exception Occured!!'
 policy = {}
 policy["defaultAction"] = "SCMP_ACT_ERRNO"
 
 #policy["syscalls"] = {}
 #policy["syscalls"]["names"] = list(syscalls)
 #policy["syscalls"]["action"] = "SCMP_ACT_ALLOW"
 #policy_json = json.dumps(policy)
 #policyjson = open('./policy_generated.json', 'w+')
 #policyjson.write(policy_json)
 
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

def removeUnknownSyscalls(syscalls):
 default_policy = ''
 with open('./data/policy/default.json', 'r') as defaultp:
  default_policy = json.load(defaultp)
 
 default_list = set(default_policy["syscalls"][0]["names"])
 final_list = list(default_list.intersection(syscalls))
 print 'DEFAULT LIST ************\n', default_list
 print 'INPUT LIST ########### \n', final_list
 return final_list


