import os,sys

class func:
	def __init__(self,name):
		self.name = name
		self.syscalls = set()
		self.callq = set()
	
	def __str__(self):
		return "{'Name' : '" + self.name + "' , 'System calls' : " + str(list(self.syscalls)) + ", 'Callq' : " + str(list(self.callq)) + '}'
	
def process_function(l,l1,l2,c, final_list):
	if '@@' in l[l1]:
		name = l[l1].split('<')[1].split('@@')[0]
	elif '@' in l[l1]:
		name = l[l1].split('<')[1].split('@')[0]
	fun = func(name)
	prev_components = [x.strip() for x in l[l1+1].split('\t')]
	for i in range(l1+2,l2):
		components = [x.strip() for x in l[i].split('\t')]
		if len(components) == 3 and len(prev_components) == 3:
			if 'syscall' in components[2]:
				cmd = prev_components[2].split(' ')
				if 'mov' in prev_components[2]:
					syscall = prev_components[2].split('mov')[1].strip().split(',')[0]
					if syscall.startswith('$0x'):
						n = syscall.split('$0x')[1]
						num = int(n,16)
						final_name = c[num].split(',')[2]
						fun.syscalls.add(final_name)
			if 'callq' in components[2]:
				if '@plt' not in components[2] and '<' in components[2]:
					function_name = components[2].split('<')[1].split('@@')[0]
					if function_name in final_list.keys():
						for f in final_list[function_name].syscalls:
							fun.syscalls.add(f)
					else:
						fun.callq.add(function_name)
				
		prev_components = components
	return fun					
		
		

f = open('glibc_objdump.txt', 'r')
l = f.readlines()
f.close()

f = open('syscall_numbers2','r')
c = f.readlines()
f.close()

i = 0
for line in l:
	i = i + 1
	if '.text' in line:
		break
l1 = -1
l2 = -1
k = i - 1
final_list = {}
for line in  l[i-1:]:
	k = k+1
	if line == '\n':
		if l1 == -1:
			l1 = k
		else:
			l2 = k - 1
			if 'section' not in l[l1]:
				fun = process_function(l,l1,l2,c,final_list)
				final_list[fun.name] = fun
				#print fun
			l1 = -1
			l2 = -1
			#if len(final_list.keys())>=400:
			#	break
#print len(final_list)
print '*********************************************************************************************************'
count = 0
for fun in final_list.keys():
	for callq in final_list[fun].callq:
		if callq in final_list.keys():
			count = count + 1
			for s in final_list[callq].syscalls:
				final_list[fun].syscalls.add(s)
	print final_list[fun]
print count

