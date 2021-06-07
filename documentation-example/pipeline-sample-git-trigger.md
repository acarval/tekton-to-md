#Tekton documentation

----
##1- Pipeline 
###1- Pipeline's params details
| NAME   |      DEFAULT      |  DESCRIPTION |
|----------|-------------|----------------------|
| repository | / | the git repo |
| branch | / | the branch for the git repo |
| revision |  | the commit id/sha for the clone action |
| pr-repository |  | The source git repo for the PullRequest |
| pr-branch |  | The source branch for the PullRequest |
| pr-revision |  | the commit id/sha for the PullRequest |
| git-access-token |  | the token to access the git repository for the clone operations |
| properties-file | output/thebuild.properties | / |
| git-credentials-json-file | output/secrets/thecredentials.json | / |
| pipeline-debug | 0 | / |
### 2- Tasks 's details
```mermaid
classDiagram
class pipeline_git_event_clone_task{
        repository : $(params.repository) 
        branch : $(params.branch) 
        revision : $(params.revision) 
        pr-repository : $(params.pr-repository) 
        pr-branch : $(params.pr-branch) 
        pr-revision : $(params.pr-revision) 
        git-access-token : $(params.git-access-token) 
        directory-name : . 
        properties-file : $(params.properties-file) 
        git-credentials-json-file : $(params.git-credentials-json-file) 
        pipeline-debug : $(params.pipeline-debug) 
    }
class pipeline_git_event_content_inspect{
        repository : $(tasks.pipeline-git-event-clone-task.results.git-repository) 
        directory-name : . 
        properties-file : $(params.properties-file) 
        git-credentials-json-file : $(params.git-credentials-json-file) 
        git-branch : $(tasks.pipeline-git-event-clone-task.results.git-branch) 
        git-commit : $(tasks.pipeline-git-event-clone-task.results.git-commit) 
        git-user : $(tasks.pipeline-git-event-clone-task.results.git-user) 
    }
   pipeline_git_event_clone_task --|> pipeline_git_event_content_inspect
```
