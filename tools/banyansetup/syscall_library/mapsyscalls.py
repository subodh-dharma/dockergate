import os,sys
import json

class func:
	def __init__(self,name):
		self.name = name
		self.syscalls = set()
		self.callq = set()
	
	def __str__(self):
		return "{'Name' : '" + self.name + "' , 'System calls' : " + str(list(self.syscalls)) + ", 'Callq' : " + str(list(self.callq)) + '}'
	@staticmethod
	def parse(dict_obj, name):
		f = func(name)
		for s in dict_obj['syscalls']:
			f.syscalls.add(s)
		for c in dict_obj['callq']:
			f.callq.add(c)
		return f

			
	def jsonify(self):
		json_obj = {}
		json_obj['syscalls'] = list(self.syscalls)
		json_obj['callq'] = list(self.callq)
		return json_obj

def follow_eax(l,start,end,reg):
	for i in range(start,end)[::-1]:
		if 'mov' in l[i] and reg in l[i]:
			components = [x.strip() for x in l[i].split('\t')]
			cmd = components[2].split(' ')
			syscall = components[2].split('mov')[1].strip().split(',')[0]
			if not syscall == None and syscall.startswith('$0x'):
				n = syscall.split('$0x')[1]
				num = int(n,16)
				return num
			else:
				return follow_eax(l,start,i,syscall.strip('(').strip(')').split('%')[1])
		
		
	
def process_function(l,l1,l2,c, final_list,exception):
	if '@@' in l[l1]:
		name = l[l1].split('<')[1].split('@@')[0]
	elif '@' in l[l1]:
		name = l[l1].split('<')[1].split('@')[0]
	else:
		name = l[l1].split('<')[1].split('>')[0]
	fun = func(name)
	print(name)
	prev_components = [x.strip() for x in l[l1+1].split('\t')]
	mov_eax_line = None
	syscall = None
	for i in range(l1+1,l2):
		if 'syscall' in l[i]:
			num = follow_eax(l,l1,i,'eax')
			if num != None:
				final_name = c[num].split(',')[1]
				fun.syscalls.add(final_name)
			else:
				exception.write(l[l1])
		if 'callq' in l[i]:
			if '<' in l[i]:
				if '@@' in l[i]:
					function_name = l[i].split('<')[1].split('>')[0].split('@@')[0]
				elif '@' in l[i]:	
					function_name = l[i].split('<')[1].split('>')[0].split('@')[0]
				if function_name in list(final_list.keys()):
					for f in final_list[function_name].syscalls:
						fun.syscalls.add(f)
				else:
					fun.callq.add(function_name)
			
			 
	return fun					
		
		

f = open(sys.argv[1], 'r')
l = f.readlines()
f.close()

f = open('syscall_list.txt','r')
c = f.readlines()
f.close()

l1 = -1
l2 = -1
k = 0
final_list = {}
if os.path.exists('output_mapping'):
	output_file = open('output_mapping','r')
	line = output_file.readline()
	dict_obj = json.loads(line)
	for d in list(dict_obj.keys()):
		final_list[d] = func.parse(dict_obj[d],d)
	
	output_file.close()
output_file = open('tmp_json_file','w')
exception_file = open('exception','a')

count_fun = 0

this_lib_list = {}

for i in  range(0,len(l)-1):
	line = l[i]	
	if line.startswith('00'):
		l1 = i
	elif (l[i+1].startswith('00') or i == len(l)-2) and l1!=-1:
		l2 = i
		if 'section' not in l[l1]:
			try:
				fun = process_function(l,l1,l2,c,final_list, exception_file)
				if fun != None:
					this_lib_list[fun.name] = fun
			except Exception as e:
				print('EXCEPTION:'+l[l1])
				exception_file.write(l[l1])
		l1 = -1
		l2 = -1
		#if len(final_list.keys())>=400:
		#	break
#print len(final_list)
print('*********************************************************************************************************')
for i in range(0,1):
	count = 0
	for fun in list(this_lib_list.keys()):
		for callq in this_lib_list[fun].callq:
			if callq in list(this_lib_list.keys()):
				count = count + 1
				for s in this_lib_list[callq].syscalls:
					this_lib_list[fun].syscalls.add(s)
		for callq in this_lib_list[fun].callq:
			if callq in list(final_list.keys()):
				count = count + 1
				for s in final_list[callq].syscalls:
					this_lib_list[fun].syscalls.add(s)
	print(count)

json_write = {}
for f in list(final_list.keys()):
	json_write[f] = final_list[f].jsonify()
for f in list(this_lib_list.keys()):
	json_write[f] = this_lib_list[f].jsonify()

print(len(list(json_write.keys())))
output_file.write(json.dumps(json_write))
output_file.close()

os.rename('tmp_json_file','output_mapping')
exception_file.close()
