# init script for the workflow

docker_img_name = sys.argv[1]

# call banyanops script




# read the banyanops output




# process the ldd output and analyze libraries
# if existing - no processing skip to next
# else read objdump of .so and generate syscall mapping




# process the nm output to identify library calls
# identify corrosponding syscalls and generate policy
