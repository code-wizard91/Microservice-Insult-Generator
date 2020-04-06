pipeline{

        agent any
        environment {
	    SERVICE_VERSION='v1'
	}
	
	stages{
		
	     stage('Ansible is Setting up Jenkins-VM, Nginx-VM, Installing Docker and Dockerswarm, on Manager and Worker Nodes '){
                steps{
		    
	            sh label: '', script: '''
                        sshpass -p ${wvmpass} ssh -o StrictHostKeyChecking=no ${ansibleuser}<<eof
			pwd 
                        cd ansible
			ansible-playbook -i inventory playbook.yml
			
		'''
                }
            }
	
	    
	     stage('Set Env variables on worker node'){
                steps{
		    
	            sh label: '', script: '''
                        sshpass -p ${wvmpass} ssh -o StrictHostKeyChecking=no ${wvmuser}<<eof
			pwd 
                        export SECRET_KEY=${SECRET_KEY}
                        export SERVICE_VERSION=${SERVICE_VERSION}
			export DATABASE_URI=${DATABASE_URI}
			export SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}
			
		'''
                }
            } 
	    	
            stage('Stack Deploy on Manager VM'){
                steps{
		    
	            sh label: '', script: '''
                        sshpass -p ${vmpass} ssh -o StrictHostKeyChecking=no ${vmuser}<<eof
			pwd 
                        export SECRET_KEY=${SECRET_KEY}
                        export SERVICE_VERSION=${SERVICE_VERSION}
			export DATABASE_URI=${DATABASE_URI}
			export SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}
			ls
			docker --version
			docker node ls
			cd insult-generator
			git pull
			echo Deploying ${SERVICE_VERSION}
			docker stack deploy --compose-file docker-compose.yaml insultgenerator
			
			
		'''
                }
            }
        }    
}
