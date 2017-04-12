import subprocess
import threading
from multiprocessing.pool import ThreadPool
def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True,shell=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

def worker(cmd):
    for path in execute([cmd]):
        print threading.currentThread().getName() + " " + path
        if 'Looping' in path:
            print 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
            break
    cmd2 = "./cleanup.sh " + cmd.split(' ')[1]
    os.system(cmd2)

# Example
threads = []
f = open("2000_list.txt",'r')
l = f.readlines()
s = threading.Semaphore()
pool = ThreadPool(processes=20)
for i in l[125:]:
    cmd = "./collector_script.sh " + i.strip()
    print cmd
    threads.append(pool.apply_async(worker,(cmd,)))

while not (all(t.ready() for t in threads)):
    pass    
        
    

