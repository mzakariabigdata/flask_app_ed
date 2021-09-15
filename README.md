# flask_app_ed

## Démarrage jenkins (agent Docker)
### Commande
    docker run -d -u root -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home/jenkins_home:/var/jenkins_home jenkins/jenkins
### install plugin
error : WorkflowScript: 2: Invalid agent type "docker" specified. Must be one of [any, label, none] @ line 2, column 13.
solution :
-   install plugins "docker" + "docker pipeline"