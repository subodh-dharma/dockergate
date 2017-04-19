# init script for the workflow
import os
import subprocess
import time
import sys
import signal


docker_img_name = sys.argv[1]

# call banyanops script
def collector_execute(cmd):
 "Execute Collector for image"
 popen = subprocess.Popen(cmd,shell=True, stdin=None, stdout=subprocess.PIPE,stderr=None)

 for stdout_line in iter(popen.stdout.readline, ""):
  yield stdout_line
 popen.stdout.close()
 return_code = popen.wait()
 if return_code:
  raise subprocess.CalledProcessError(return_code, cmd)

def worker(cmd):
 "Check for completion of collector"
 for path in collector_execute([cmd]):
   if 'Looping in ' in path:
    print "Looks like script collection is complete"
    break
  #cmd2 = "./cleanup.sh " + cmd.split(' ')[1]
  #os.system(cmd2)

worker("sudo ./tools/banyansetup/collector_script.sh "+docker_img_name)
print 'Process killed..' 


# read the banyanops output




# process the ldd output and analyze libraries
# if existing - no processing skip to next
# else read objdump of .so and generate syscall mapping




# process the nm output to identify library calls
# identify corrosponding syscalls and generate policy
