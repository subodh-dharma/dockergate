import subprocess
import sys
f = open('data/community-docker-2000.txt','r')

for line in f.readlines()[39:]:
	i = open('image_index','r')
	flag = False
	for l in i.readlines():
		if line == l:
			flag = True
			break	
	if flag:
		continue
	if "ubuntu" not in line and "debian" not in line:
		continue
	print 'analysing ' + line.strip()
	p = subprocess.Popen(["sudo python dockergate.py "+line.strip()],shell=True, stdout=subprocess.PIPE)
	while p.poll() is None:
    		l = p.stdout.readline() # This blocks until it receives a newline.
    		sys.stdout.write(l)	
	p.stdout.readlines()
	
	cleanup = subprocess.Popen(["sudo ./tools/banyansetup/cleanup.sh "+line],shell=True, stdin=None, stdout=subprocess.PIPE,stderr=None)
	output = cleanup.stdout.readlines()
	print '*****'
