pipeline{

        agent any
        environment {
	    SERVICE_VERSION='v2'
	}
        stages{
	    
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
