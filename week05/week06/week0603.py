from github import Github
import requests
g = Github("59fad4a0d3fb3d6c1c3d4c791a2de16891b3f952")
#for repo in g.get_user().get_repos():
    #print(repo.name)

repo = g.get_repo("paulacduffy/week06lab")
#print(repo.clone_url)
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

newContents = contentOfFile + " more stuff \n"
#print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents
,fileInfo.sha)
#print (gitHubResponse)

