pipeline{

        agent any
        environment {
	    SERVICE_VERSION='v1'
	}
        stages{
            stage('Stack Deploy on Manager VM'){
                steps{
		    
	            sh label: '', script: '''
                        sshpass -p ${vmpass} ssh -o StrictHostKeyChecking=no ${vmuser}<<eof
			pwd 
                        export SECRET_KEY=${SECRET_KEY}
                        export SERVICE_VERSION=${SERVICE_VERSION}
			export DATABASE_URI=${DATABASE_URI}
			export SQLALCHEMY_DATABASE_URI=${SQLALCHEMY_DATABASE_URI}
			ls  -a
			docker --version
			sh sudo docker stack deploy --compose-file docker-compose.yaml insultgenerator
			
		'''
                }
            }
        }    
}
