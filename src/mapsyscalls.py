import subprocess
import sys

file_name = sys.argv[1]

output = subprocess.check_output(['nm','-D',file_name])
output_list = output.splitlines()

for value in output_list:
 if 'U' not in value:
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
    print 'Doesn\'t exist in lib :', value

#print output_list
print syscalls
