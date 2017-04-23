import os,sys

file_name = sys.argv[1]
'''if os.path.exists('index'):
	index_file = open('index', 'r')
	for line in index_file.readlines():
		if file_name in line:
			print 'Already Done'
			sys.exit(0)'''
f = open('exception','a')
f.write(file_name + '\n')
f.close()

os.system('objdump -D --section=.text ' + file_name + ' >tmp')
os.system('python mapsyscalls.py tmp')

#index_file = open('index','a')
#index_file.write(file_name + '\n')
#index_file.close()
