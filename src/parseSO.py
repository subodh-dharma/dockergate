import re
import json
import pprint

class funcsyscall:
 'System calls of library functions'
 
 def __init__(self,fname):
  self.name = fname
  self.syscalls = set()
  self.callq = set() 
  self.exceptions = list() 
 def __str__(self):
  return "{ \"function\": '"+self.name+"' , \"syscalls\": "+ str(list(self.syscalls)) + ", \"callqs\": " + str(list(self.callq)) + "}"
 def __repr__(self):
   return self.__str__()

# List of jump instructions
jump_instr = ['callq','je', 'jz', 'jle', 'jnz', 'jne', 'js', 'ja', 'jnbe', 'jae', 'jnb', 'jb', 'jnae', 'jbe', 'jna', 'jxcz', 'jc', 'jnc', 'jo', 'jno', 'jp','jpe', 'jnp', 'jpo', 'jns', 'jg', 'jnle', 'jge', 'jnl', 'jl', 'jnge', 'jle', 'jng']

func_list = []
except_list = []

fo = open('./data/chdir.log')
line = fo.readline()

while line:
 # header of function - to get the func name
 tempfunc = funcsyscall('default')
 matchexpr1 = re.search(r'\w*\s+<\w*@@\w*[.\d]*>:', line,re.I)
 if matchexpr1:
  #print line
  result = re.compile('<\w*')
  # strip the func name from the line
  matchexpr2 = re.search('<\w*', line)
  if matchexpr2:
   func_name = matchexpr2.group().strip('<')
   tempfunc.name = func_name
   #print func_name
  while line: 
  # finding the mov stmt before the syscall
   if 'mov' in line:
    prev_line = line
    line = fo.readline()
   # check if previous line was related to system call
    if 'syscall' in line:
     syscall_hex = prev_line.split('mov')[1]
     syscall_hex = syscall_hex.lstrip().rstrip()
    #confirm if syscall - check register is EAX
     if 'eax' in syscall_hex.split(',')[1]:
      syscall_hex = syscall_hex.split(',')[0]
      try:
       syscall_hex = syscall_hex.split('$0x')[1]
       syscall_int = int(syscall_hex,16)
       #print syscall_int
       tempfunc.syscalls.add(syscall_int)
       #print tempfunc
       #func_list.append(tempfunc)
      except:
       #print 'EXC', prev_line
       except_list.append('EXC\n'+prev_line+line)
      func_list.append(tempfunc)
     else:
      continue
   elif any( jump in line for jump in jump_instr):
    jump_call = line.split(' ')
    j = jump_call[len(jump_call) - 1].rstrip().lstrip()
    tempfunc.callq.add(j) 
   line = fo.readline()
   if not line.strip():
    break
 line = fo.readline()


json_array = {"functions":[]}


for f in func_list:
 json_array["functions"].append(f)

jsonfile = open('libc.json', 'w+')
json_str = str(json_array)
json_str = json_str.replace("'",'"')
jsonfile.write(json_str)
jsonfile.close()

#print json_array
with open('libc.json') as jsonread:
 data = json.load(jsonread)
 pprint.pprint(data)


#print json.dumps(jsonread.readlines()[0], indent=4, separators=(',', ':'))


for e in except_list:
 print e
