from sets import Set
from types import NoneType

from github import Github

g = Github("user", "password")

# for repo in g.get_user().get_repos():
#     print repo.name

for org in g.get_user().get_orgs():
    print "======================================="
    print org.name
    for repo in org.get_repos():
        if "requirement-analysis" in repo.name:
            print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            print repo.name
            commits=repo.get_commits()
            authors=Set()
            for commit in commits:
                if type(commit.author) != NoneType and commit.author.login != u'Eisenbarth':
                    authors.add(commit.author.login)
            print authors


