## Index
[Brief](#brief)
   * [My Solution](#mysolution)
   
[Risk Assessment and Product Backlog](#riskbacklog)
   * [Risk Assessment](#spr1)
   * [Risk Assessment Table](#risktable)
   * [User Stories](#userstories)

[Sprints & Planning](#sprone)
   * [Trello Board Sprint 1.0](#sprone)
     
[My Deployment Method](#deploymentmethod)
   * [What I used](#techused)

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

### Service #1

The core service – this will render the Jinja2 templates to interact with your application, it will also be responsible for communicating with the other services, and finally for persisting some data in an SQL database.

### Service #2 and #3

These will both generate a random “Object”. The first object generated is a random beggining of a insulting sentance, the second object
is a randomly generated insult

### Service #4

This service will also create an “Object” using what is generated from service 2 and 3. Essentially this service brings together the responses from service 2 and 3.

### Service #5

This service will attach a joke to the insult which is generated.

### Anisble

Ansible will be used to set up the environments for each remote vm, So this means installing and configuring docker, docker-compose, adding required users and configuring access for Jenkins on the Manager node and Worker node, Setting up Jenkins VM auto generating access and SSH keys, Ansible was also used to setup the Nginx Reverse Proxy server (VM) copy my configured nginx config to the remote host and resart the server allowing me to load balance all my services through an Nginx server thus decreasing redundancy.

<a name="mysolution"></a>
### Solution

I decided to create a Random Insult & Joke Generator with a Microservice architecture, My application will have 5 services not including Jenkins, Managed MYSQL db, Nginx server, Ansible Server.

- Service 1 of my project is essentially the front-end where the insult that is gemerated will be shown to the user.
- Service 2 and 3 will be services that generate the random insult.
- Service 4 is the back-end that puts them together and sends the complete insult to the front end, the insult is then stored inside a     database. 
- Service 5 will connect to an external API hosted by rapidapi.com that generates a random joke, it will then perform some logic to       convert the json into text and send the response as plain text for the front-end to use.

- I will be using Ansible as a way to stage all my environments and prepare them to run my services.
- I will use Jenkins to build a testing and deployment pipeline using Jenkinsfile that will be triggered using Git/Github webhook
- Nginx will be used as a Reverse Proxy to load balance all my services running on Docker Swarm

<a name="riskbacklog"></a>
## Risk Assessment and Product Backlog


<a name="spr1"></a>
## MosCow Prioritisation and Product Backlog (Trello Board) (Sprint 1)

The first list you see is the product backlog, I prioritised the list depending on the MVP of the project, this was done using coloured labels which represent the priority of each task (See labels below)

![Trello Image](/Images/sprint1.jpg)
![Trello Image](/Images/labels.jpg)

<a name="risktable"></a>
## Risk Assessment Table
![Risk Assessment Table](/Images/risktable1.jpg)


<a name="userstories"></a>
## User Stories (Users and Developers)

The User Stories was also done on Trello, I listed all the use-cases for the product in the perspective of a user and a developer.
(Click image for higher quality image) 

![UserStories](/Images/userstories.jpg)


<a name="sprone"></a>
## MosCow Prioritisation and Product Backlog (Trello Board) (Sprint 1)

Here is the First Sprint I did after defining the main requirements of the project. (Click image for higher quality image).

![Trello Image](/Images/sprint1.jpg)


<a name="deploymentmethod"></a>
## Deployment

![Deployment Pipeline](/Images/pipeline.jpg)

The Deployment pipeline for this Flask application was done using Git/Github for source control and automating that process using
webhooks with Jenkins FINISH THIS HERE

## How the process looks

Here is the actual test and building process taking place.

![Jenkins Coverage Report](/images/automation.jpg)

<a name="visrep"></a>
## Visual Representation of App


<a name="techused"></a>
### List of Technologies Used

* MySQL for Application Database
* Python - Coding in Flask
* Flask - Framework 
* Jenkins - CI Server
* Docker / Docker Swarm
* [Github Project](https://github.com/code-wizard91/Performance-Motors) - Version Control System
* [Trello Board](https://trello.com/b/5RcaZXRp) - Project Tracking Board
* Azure Services (MySQL Azure DB, Azure VM)

<a name="eval"></a>
## Retrospect

Eval will go here


<a name="authorsinv"></a>
## Authors

Mahboob Ali

<a name="acknowledgements"></a>
## Acknowledgements

* Jay Grindrod
