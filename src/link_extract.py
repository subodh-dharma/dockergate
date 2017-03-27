import os
import sys
import json
import urllib
from github import GitHub

git_token = os.environ['GITTOKEN']
gitapi = GitHub(access_token=git_token)

files = os.listdir('../nvm')
#files = os.listdir('../dockerlibrary')
count = 0
branch_path = ''
for f in files:
 fo = open('../nvm/'+f)
 #fo = open('../dockerlibrary/'+f)
 print fo.name
 line = fo.readline()
  
 while line:
  if 'GitRepo' in line:
   print line
   splitlist = line.split('/',5)
   repo_owner = splitlist[3]
   repo_name = splitlist[4].split('.git\n',1)[0]
  
  if 'GitFetch' in line:
   branch_path = line.split('/',3)[2].rstrip()
   print 'BRANCH', branch_path
  if 'Directory' in line:
   #print line   
   tag = (line.split(' ', 1)[1]).rstrip()
   print 'TAG', tag
   file_path = tag + '/Dockerfile'
   print 'FILE PATH', file_path
   print repo_owner, repo_name
   if (branch_path == ''):
    file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path).get()
   else:
    file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path+'?ref='+branch_path).get()
   download_file = urllib.URLopener()
   print 'RAW GIT', file_git.download_url
   download_file.retrieve(file_git.download_url, './downloads/Dockerfile_'+repo_name+'_'+tag.replace('/','_'))
   count = count + 1
   print count

  line = fo.readline()
 branch_path = '' 
 fo.close()
