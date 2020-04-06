## Index
[Brief](#brief)
   * [My Solution](#mysolution)
   * [Services](#myservices)
   
[Risk Assessment and Product Backlog](#riskbacklog)
   * [Risk Assessment](#spr1)
   * [Risk Assessment Table](#risktable)
   * [User Stories](#userstories)

[Sprints & Planning](#spr1)
   * [Trello Board Sprints](#spr1)
     
[Deployment Method](#deploymentmethod)
   * [Jenkins CI/CD Server](#ci)
   * [Ansible Server](#ans)
   * [Docker Swarm](#dswarm)
   * [What I used](#techused)

[Testing Pytest](#test)

[Visual Representation of my Solution](#visrep)

[Retrospective](#eval)

[Authors](#authorsinv)

[Acknowledgements](#acknowledgements)

<a name="brief"></a>
## The Product Brief

To create app using:
* Software Development with Python
* CI/CD using Jenkins, Ansible pipeline (Seperate Cloud Services)
* Nginx as reverse proxy
* Managed MySQL database on the cloud
* Docker and Orchestration using Docker-Swarm, Split app into micro-services in the cloud with built in redundancies such as Load-Balancing behind Nginx. (One Manager node, One Worker Node in Swarm)
* Use Ansible to set up all VM's (Installing Dependencies and applications) using Playbook
* Use Jenkins to set up multiple stages in the pipeline; Staging, Testing, Building and Deployment and implement a Git Webhook as a
trigger
* Implement Cloud Fundamentals such as test driven development, Continuous Integration and deployment, and a SCRUM based methodology 
* Micro-service oriented architecture composed of at least 4 services that work together and services 2,3,4 should be easily interchangeable using versioning on Dockerhub.

<a name="mysolution"></a>
### Solution

I decided to create a Random Insult & Joke Generator with a Microservice architecture, My application will have 5 services not including Jenkins, Managed MYSQL db, Nginx server, Ansible Server and Docker Swarm

- Service 1 of my project is essentially the front-end where the insult that is generated will be shown to the user.
- Service 2 and 3 will be services that generate the random insult.
- Service 4 is the back-end that puts them together and sends the complete insult to the front end, the insult is then stored inside a     database. 
- Service 5 will connect to an external API hosted by rapidapi.com that generates a random joke, it will then perform some logic to       convert the json into text and send the response as plain text for the front-end to use.
- Service 2,3,4 can be changed to V2 so it returns a greeting and a compliment instead of an insult, also if a special parameter is met   within the logic of service 4 the user gets a surprise brain teaser
- I will be using Ansible as a way to stage all my environments and prepare them to run my services.
- I will use Jenkins to build a testing and deployment pipeline using Jenkinsfile that will be triggered using Git/Github webhook
- Nginx will be used as a Reverse Proxy to load balance all my services running on Docker Swarm


<a name="myservices"></a>
## My Micro-service architecture

### Service #1

The core service – this will render the Jinja2 templates to interact with the application, it will also be responsible for communicating with the other services, and finally for persisting some data in an SQL database. Each service is its own Flask Application and has its own directory and files (See Below)

![Files and folders](/Images/structure1.jpg)
![Front end structure](/Images/structure3.jpg)

Here is how the front end looks when recieving requests from other services.

![f-look](/Images/service1.jpg)

### Service #2 and #3

These will both generate a random “Object”. The first object generated is a random beggining of a insulting sentance, the second object
is a randomly generated insult

Below is the V1 version of service 2

![s2](/Images/service2.jpg)

Below is the alternate v2 version of service 2

![s2v2](/Images/service2v2.jpg)

Below is the V1 version of service 3

![s3](/Images/service3.jpg)

Below is the alternate v2 version of service 3

![s3v2](/Images/service3v2.jpg)


### Service #4

This service will also create an “Object” using what is generated from service 2 and 3. Essentially this service brings together the responses from service 2 and 3.

Below is the V1 version of service 4

![s4](/Images/service4.jpg)

Below is the alternate v2 version of service 4

![s4v2](/Images/service4v2.jpg)

### Service #5

This service will attach a joke to the insult which is generated.

Below is service 5 it generates request using an external API

![s5](/Images/service5.jpg)


<a name="riskbacklog"></a>
## Risk Assessment and Product Backlog


<a name="spr1"></a>
## MosCow Prioritisation and Product Backlog (Trello Board) (Sprint 1)

The first list you see is the product backlog, I prioritised the list depending on the MVP of the project, this was done using coloured labels which represent the priority of each task (See labels below)

![Trello Image](/Images/sprint1.jpg)
![Trello Image](/Images/labels.jpg)

## Sprint 1 (Cont..)

Below I started on the tasks that would get me the Minimum Viable Product, I Created all the main services and made sure all the endpoints for each service was working, I then moved onto creating the docker-compose file that I would use to create and test my app on a Docker Swarm, I also connected a Managed Mysql DB to the front-end service to persist the random insults. Before doing all this I made sure to create a develop branch on my Github repository that I merged with the Master branch at the end.

![Trello Image](/Images/sprint1.1.jpg)

## Sprint 1 ( COMPLETED )

As you can see I successfully completed all the tasks listed on my first sprint and moved them over to my done list on my Kanban Board.

![Trello Image](/Images/sprint1.2.jpg)

## Sprint 2

Here is my second Sprint where I aimed to complete a lot of the tasks that I thought would take a long time due to the complexity of the automation I was trying to achieve using Ansible and Jenkins. I also found Nginx hard to conceptualise as reverse proxies are a new concept to me. I also finished the alternating service that can be easily switched by changing the version number in my Jenkinsfile on Github, this change will be detected by my Jenkins server and will update all the services running on the Swarm Automatically. 

![Trello Image](/Images/sprint2.jpg)

## Sprint 2 ( COMPLETED )

![Trello Image](/Images/sprint2.1.jpg)

![Trello Image](/Images/sprint3.jpg)

<a name="risktable"></a>
## Risk Assessment Table
![Risk Assessment Table](/Images/risktable1.jpg)


<a name="userstories"></a>
## User Stories (Users and Developers)

The User Stories was also done on Trello, I listed all the use-cases for the product in the perspective of a user and a developer.
(Click image for higher quality image) 

![UserStories](/Images/sprint1.jpg)

<a name="deploymentmethod"></a>
## Deployment Methodology

![Deployment Pipeline](/Images/pipeline.jpg)

The Deployment pipeline starts with setting up the VM environments using Ansible, a Github trigger on commit will start the test and build process within Jenkins, Jenkins will then deploy the Swarm and nodes to the cloud, Data will also be persisted in a managed MYSQL database, Nginx will Load Balance all traffic coming in across the nodes. Below is an image of all the VM's and resources on Microsoft Azure.

![VM](/Images/vms.jpg)

<a name="ci"></a>
## Jenkins CI Server

Jenkins was used to securely ssh into the deployment VM's which are running the Docker Swarm Manger node and the worker node to deploy the app and set key environment variables.

Before the app is deployed the app must pass the test (See Below) if the tests pass the build will continue.

Heres the test running before deployment on Jenkins

![testjenk](/Images/test3.jpg)

I created a Jenkinsfile to define each stage of the deployment, this file is read by the Jenkins server and used to deploy the app.

Ansible was used to setup the Jenkins CI server thus automating the entire process. 

The version of the app can be changed from v1 to v2 using the SERVICE_VERSION variable and this will change how the application works. 

Environment Variables were stored inside the Jenkins CI server as global variables so I could then reference them within my Jenkinsfile. See below for a more in-depth look.


![Jenkinsfile](/Images/jenk.jpg)

Below is an image snippet of the build process running after being triggered by a Git Commit

![Jenkinsfile](/Images/jenkrunning.jpg)


<a name="ans"></a>
## Ansible Software Provisioning and Config Management

Ansible is a very useful tool as it allowed me to set up all my cloud VM's with the Packages and Softwares that my App and services need to run, this includes; installing Jenkins and setting up my user automatically, Installing and fully configuring my Nginx Load Balancing server, Installing Docker and Docker-Compose on my manager and worker vm to use with Docker Swarm. 

I set up my Ansible by creating specific roles that would be executed on each VM, roles are important as they allow you to reuse configurations on multiple hosts (SEE BELOW)

![Ansible](/Images/ansible.jpg)

As you can see in the folder structure I have a directory called roles, inside this directory I have multiple roles that contain specific configurations etc. Docker for installing Docker and Compose, Dockermanager and Dockerworker sets up my Node's for Docker Swarm, Jenkins for setting up my Jenkins Server, Git for setting up and installing Git and Nginx to set up my reverse proxy load balancer.

(See below)

![Ansible roles](/Images/ansible2.jpg)

The docker directory contains the inventory file which holds all the VM IP's that ansible will run on, also the Playbook file which ansible references when installing dependancies, this essentially holds each task that Ansible will run. Inside the roles folder I defined each role depending on the specific task it would perform (docker role installs docker, Nginx installs Nginx) inside each role folder is a "main.yaml" that holds all the configurations for each role.  

## Inventory File

For the inventory file I created host groups depending on the task that they perform, this makes it easier to reference in the Playbook file, each section has the VM Ip's that Ansible will access and variables Ansible will use when accessing a remote host.

![Ansible roles](/Images/ansible4.jpg)

## Playbook file

The Playbook File has services and tasks that Ansible needs to perform on each host. Below you can see how I reference the Roles I created before, ansible will run each role in the remote host. 

![Ansible roles](/Images/ansible3.jpg)

Here is an image of Ansible running its Plays.

![Ansible running](/Images/ansrunning.jpg)


<a name="dswarm"></a>
## Docker-Swarm

To split my app into micro-services I created Docker Images of each service and uploaded each version to Dockerhub, this enables me to switch versions very easily, I used each of these images in the compose file below, I then used these images and Docker-Compose to create a Docker Swarm of containers to increase my apps resiliance and reduce down-time and possible redundancies. 

Below is an image of the swarm running on both the manager and the worker nodes. Click image for a better look. (Terminal at the top is the manager node, Terminal at the bottom is the worker node

![Running Swarm](/Images/swarmrunning.jpg)

Below is an image of a Dockerfile I used to create my images.

![Dockerfile](/Images/structure2.jpg)

In the compose file I defined how many replicas of the service I want running in the Swarm

![Docker Compose](/Images/dockercompose.jpg)

<a name="test"></a>
### Testing Pytest
Heres the coverage report Generated and the testing file, Note: I only tested my Front-End Service as my other services had all their ports closed, after a lot off errors and hours I decided to run simpler requests tests.

![test](/Images/test.jpg)

![test](/Images/test1.jpg)

Heres the test running before deployment on Jenkins

![test](/Images/test3.jpg)


<a name="techused"></a>
### List of Technologies Used

* MySQL for Application Database
* Python - Coding in Flask
* Flask - Framework
* Nginx
* Pytest
* Ansible
* Jenkins - CI Server
* Docker / Docker Swarm
* [Github Project](https://github.com/code-wizard91/insult-generator) - Version Control System
* Trello Board
* Azure Services (MySQL Azure DB, Azure VM)

<a name="visrep"></a>
## Visual Representation of App

As you can see the app is working and generating random insults using a micro-service architecture and with multiple backend services to steamline deployment and manage server load and redundancies

![Visual Rep](/Images/visrep.jpg)


<a name="eval"></a>
## Retrospect

Whilst working on this project I learnt a lot about all the different services and technologies that I used, I really enjoyed using Ansible to provision my VM environments and really enjoyed using Docker-Swarm to scale my application, Overcoming hurdles was one of situations I found myself in as I had to research and learn every step of the way, But this was the main reason I learnt so much and finished this project.

Looking back I would start my testing from the beggining of the project as testing is one of my weaknesses that I need to improve, I also need to use the people around me when I am stuck with something as some of the issues were very small and easy to fix.

Finally I would definately recommend using these technologies as automation is the future and a very exciting one indeed.


<a name="authorsinv"></a>
## Authors

Mahboob Ali

<a name="acknowledgements"></a>
## Acknowledgements

* Jay Grindrod - Thank you for all your help, and putting up with all my random questions, You are a true mentor and someone that is amazing at relaying information and knownledge, I will honestly miss your coding sessions and of course the football banter! 
