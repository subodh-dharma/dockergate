import os
import sys
import json
import urllib
from github import GitHub

git_token = os.environ['GITTOKEN']
gitapi = GitHub(access_token=git_token)

files = os.listdir('../dockerlibrary')

fo = open('../dockerlibrary/adminer')
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
  file_git = gitapi.repos(repo_owner)(repo_name).contents(file_path).get()
  download_file = urllib.URLopener()
  download_file.retrieve(file_git.download_url, './downloads/Dockerfile_'+repo_name+'_'+tag.replace('/','_'))
  print file_path 
 line = fo.readline()
fo.close()

#for file in files:
# print(file)
# fo = open('../dockerlibrary/'+file, "r")
# str = fo.read()
# print str
# fo.close()

#git_user = 'subodh-dharma'


file_name = gitapi.repos('TimWolla')('docker-adminer').contents('/4.3/Dockerfile').get();
#print file_name.download_url
#download_file = urllib.URLopener()
#download_file.retrieve(file_name.download_url, 'Dockerfile_docker-adminer')
