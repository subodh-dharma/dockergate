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
 repo_owner = line.split('/')[0] 
 repo_name = line.split('/')[1].rstrip()
 file_path = '/Dockerfile'
 print 'FILE PATH', file_path
 print repo_owner, repo_name
 if (branch_path == ''):
  file_git = gitapi.repos(repo_owner)(repo_name).contents('./Dockerfile').get()
 else:
  file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path+'?ref='+branch_path).get()
 download_file = urllib.URLopener()
 download_file.retrieve(file_git.download_url, './downloads1/Dockerfile_'+repo_owner + '_' +repo_name)
 count = count + 1
 print count

 line = fo.readline()
branch_path = '' 
fo.close()
