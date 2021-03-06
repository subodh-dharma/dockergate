# init script for the workflow
import os
import subprocess
import sys
sys.path.append('./src')
import mapsyscalls


docker_img_name = sys.argv[1]
index = open('image_index','a')
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
   print path
   if 'Looping in ' in path:
    print "Looks like script collection is complete"
    break
  #cmd2 = "./cleanup.sh " + cmd.split(' ')[1]
  #os.system(cmd2)

worker("./tools/banyansetup/collector_script.sh "+docker_img_name)
print 'Process killed..' 


# read the banyanops output

#output_dir = os.environ.get('BANYAN_OUTPUT_DIR')
output_dir =  './test_env/' + docker_img_name + '/output/hostcollector/banyanout'


'''ldd_file_path = str(output_dir) +"/print_file"
for file in os.listdir(ldd_file_path):
    if file.endswith(".txt"):
        ldd_file_path = ldd_file_path +'/'+file'''

nm_file_path = output_dir+"/run_nm"
for file in os.listdir(nm_file_path):
    if file.endswith(".txt"):
        nm_file_path = nm_file_path +'/'+file

print nm_file_path

f = open(nm_file_path,'r')
line = f.readline()
if 'NA' in line:
 index.close()
 print 'No analysis for ' + sys.argv[1]
 cleanup = subprocess.Popen(["sudo ./tools/banyansetup/cleanup.sh "+docker_img_name],shell=True, stdin=None, stdout=subprocess.PIPE,stderr=None)
 output = cleanup.stdout.readlines()
 print '*****'
 exit()

# process the ldd output and analyze libraries
# if existing - no processing skip to next
# else read objdump of .so and generate syscall mapping

##   YET TO CONVERT
mapsyscalls.copy_new_mapping(nm_file_path)


# process the nm output to identify library calls
# identify corrosponding syscalls and generate policy

print 'Converting nm output to json policy:'
mapsyscalls.map_nm_2_sys(nm_file_path)
print 'Policy Generated!'
index.write(sys.argv[1] + '\n')
index.close()

os.rename('policy_generated.json','data/policy/' + docker_img_name.replace('/','_') + '.json')

## calling clean up
## delete image after scanning, delete all test_env data


