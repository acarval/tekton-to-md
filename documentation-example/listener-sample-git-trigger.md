#Tekton documentation

----
##1- TriggerTemplate 
###1- TriggerTemplate's params details
| NAME   |      DEFAULT      |  DESCRIPTION |
|----------|-------------|----------------------|
| git-access-token | / | the token to access the git repository for the clone operations |
| repository |   | The git repo |
| branch | / | the branch for the git repo |
| revision |   | the commit id/sha for the clone action |
| pr-repository |   | The source git repo for the PullRequest |
| pr-branch |   | The source branch for the PullRequest |
| pr-revision |   | the commit id/sha for the PullRequest |
| triggerName | git-pr-process | / |
| pipeline-debug | 0 | / |
----
##2- TriggerBinding triggerbinding-git-trigger-manual

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(params.repositoryForManualTrigger)  |
| branch  |  master  |
| triggerName  |  manual-trigger  |
----
##4- TriggerBinding triggerbinding-git-trigger-github-pr

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.pull_request.base.repo.clone_url)  |
| branch  |  $(event.pull_request.base.ref)  |
| pr-repository  |  $(event.pull_request.head.repo.clone_url)  |
| pr-branch  |  $(event.pull_request.head.ref)  |
| pr-revision  |  $(event.pull_request.head.sha)  |
| triggerName  |  github-pullrequest  |
----
##5- TriggerBinding triggerbinding-git-trigger-github-commit

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.repository.url)  |
| revision  |  $(event.head_commit.id)  |
| branch  |  $(event.ref)  |
| triggerName  |  github-commit  |
----
##8- TriggerBinding triggerbinding-git-trigger-grit-mr

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.object_attributes.target.git_http_url)  |
| branch  |  $(event.object_attributes.target_branch)  |
| pr-repository  |  $(event.object_attributes.source.git_http_url)  |
| pr-branch  |  $(event.object_attributes.source_branch)  |
| pr-revision  |  $(event.object_attributes.last_commit.id)  |
| triggerName  |  grit-mergerequest  |
----
##9- TriggerBinding triggerbinding-git-trigger-grit-commit

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.repository.git_http_url)  |
| revision  |  $(event.checkout_sha)  |
| branch  |  $(event.ref)  |
| triggerName  |  grit-commit  |
----
##12- TriggerBinding triggerbinding-git-trigger-bitbucket-pr

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.pullrequest.destination.repository.links.html.href)  |
| branch  |  $(event.pullrequest.destination.branch.name)  |
| pr-repository  |  $(event.pullrequest.source.repository.links.html.href)  |
| pr-branch  |  $(event.pullrequest.source.branch.name)  |
| pr-revision  |  $(event.pullrequest.source.commit.hash)  |
| triggerName  |  bitbucket-pullrequest  |
----
##13- TriggerBinding triggerbinding-git-trigger-bitbucket-commit

###1- TriggerBinding's params details
| NAME   |      VALUE      |
|----------|-------------|
| repository  |  $(event.repository.links.html.href)  |
| revision  |  $(event.push.changes[0].new.target.hash)  |
| branch  |  $(event.push.changes[0].new.name)  |
| triggerName  |  bitbucket-commit  |
