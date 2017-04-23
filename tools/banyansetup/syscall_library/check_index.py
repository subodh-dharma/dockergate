import json
import sys
import subprocess
import os

def recursive_ldd(current_list,filename,is_library):
	if filename.split('/')[-1].split('.')[0] in current_list:
		return True
	else:
		ldd_out = subprocess.getoutput('ldd ' + filename)
		file_list = ldd_out.split('\n')
		final_list =[]
		for f in file_list:
			f = f.split(' ')
			for l in f:
				if '/' in l:
					print(l.strip())
					final_list.append(l.strip())
		for l in final_list:
			recursive_ldd(current_list, l, True)

		print('All libraries found')
		if is_library:
			print('Now mapping current library ' + filename)
			os.system('python driver.py ' + filename)
			print('Done')
			current_list.append(filename.split('/')[-1].split('.')[0])
			input_file = open('index','a')
			input_file.write(filename + '\n')
			input_file.close()
				
		return True

input_file = open('index','r')
current_list = input_file.readlines()
input_file.close()
current_list = [line.split('/')[-1].split('.')[0] for line in current_list]

#input an executable binary to get all its libraries mapped
print(recursive_ldd(current_list,sys.argv[1],False))

		
	

