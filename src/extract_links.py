import os
import sys
import json
import urllib
from github import GitHub

git_token = os.environ['GITTOKEN']
gitapi = GitHub(access_token=git_token)

files = os.listdir('../dockerlibrary')
count = 0
for f in files:
 fo = open('../dockerlibrary/'+f)
 print fo.name
 line = fo.readline()
  
 while line:
  if 'GitRepo' in line:
   print line
   splitlist = line.split('/',5)
   repo_owner = splitlist[3]
   repo_name = splitlist[4].split('.',1)[0]
 
  if 'Directory' in line:
   #print line   
   tag = (line.split(' ', 1)[1]).rstrip()
   file_path = '/' + tag + '/Dockerfile'
   print file_path
   print repo_owner, repo_name
   file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path).get()
   download_file = urllib.URLopener()
   download_file.retrieve(file_git.download_url, './downloads/Dockerfile_'+repo_name+'_'+tag.replace('/','_'))
   count = count + 1
   print count

  line = fo.readline()
  
 fo.close()
