import subprocess
import sys
import json

file_name = sys.argv[1]

output = subprocess.check_output(['nm','-D',file_name])
output_list = output.splitlines()

for value in output_list:
 if 'U' not in value:
  print value
  output_list.remove(value)
print '***'   

for index in range(0, len(output_list)):
 if 'U' in output_list[index]:
  output_list[index] = output_list[index].split('U')[1].strip()

libc = ''

with open('./data/output_mapping', 'r') as libcfile:
 libc = eval(libcfile.read())

syscalls = set()
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
   print 'Doesn\'t exist in lib :', value

#print output_list
#print syscalls

policy = {}
policy["defaultAction"] = "SCMP_ACT_ERRNO"
policy["syscalls"] = {}
policy["syscalls"]["names"] = list(syscalls)
policy["syscalls"]["action"] = "SCMP_ACT_ALLOW"

#print policy

policyjson = open('./policy.json', 'w+')
policyjson.write(str(policy))
policyjson.close()

