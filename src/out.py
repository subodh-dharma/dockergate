import os
import sys
import json
import urllib
from github import GitHub

git_token = os.environ['GITTOKEN']
gitapi = GitHub(access_token=git_token)

#files = os.listdir('../nvm')
#files = os.listdir('../dockerlibrary')
count = 0
branch_path = ''

f = open('2000_list.txt','r')
  
for line in f.readlines():
 if len(line.split('/')) < 2:
  continue
 repo_owner = line.split('/')[0] 
 repo_name = line.split('/')[1].rstrip()
 file_path = '/Dockerfile'
 print 'FILE PATH', file_path
 print repo_owner, repo_name
 download_url = ''
 if (branch_path == ''):
  try:
   file_git = gitapi.repos(repo_owner)(repo_name).contents('Dockerfile').get()
   download_url = file_git.download_url
  except Exception , e:
   print 'NOT FOUND FOR', line
   continue
 else:
  file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path+'?ref='+branch_path).get()
 download_file = urllib.URLopener()
 print download_url
 download_file.retrieve(download_url, './downloads1/Dockerfile_'+repo_owner + '_' +repo_name)
 count = count + 1
 print count

 #line = fo.readline()
branch_path = '' 
#fo.close()
