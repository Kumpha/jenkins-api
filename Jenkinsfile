def vm2=[:]
vm2.name = 'vm2'
vm2.host = '192.168.56.101'
vm2.user = 'kumpha'
vm2.port = 22
vm2.password = '123456'
vm2.allowAnyHosts = true

def vm3=[:]
vm3.name = 'vm3'
vm3.host = '192.168.56.102'
vm3.user = 'kumpha'
vm3.port = 22
vm3.password = '123456'
vm3.allowAnyHosts = true


pipeline {
    agent any

    stages {
        stage('UnitTest on Vm2') {
            steps {
                echo 'Testing..'
                 script {
                    echo 'git pull'
                    sshCommand(remote: vm2, command: 'cd jenkins-api/ && git pull')
                
                    echo 'Run unit test'
                    sshCommand(remote: vm2, command: 'cd jenkins-api/ && python3 unit_test.py')
                }
            }
        }
        stage('Build on Vm2') {
            steps {
                script {
                    echo 'Building..'
                    sshCommand(remote: vm2, command: "cd jenkins-api/ && echo '123456' | sudo -S docker-compose up -d --build")
                }
            }
        }
        stage('RobotTest on Vm2') {
            steps {
                script {
                    echo 'git pull'
                    sshCommand(remote: vm2, command: 'cd Robot-jenkins/ && git pull')

                    echo 'Testing..'
                    sshCommand(remote: vm2, command: "python3 -m robot Robot-jenkins/test_api.robot")
                }
            }
        }
        stage('Push image to gitlab Registry on Vm2') {
            steps {
                script {
                    echo 'gitlab login & push'
                    sshCommand(remote: vm2, command: "cd api-jenkins-assignment/ \
                    && echo '123456' | sudo -S docker login registry.gitlab.com \
                    && echo 'Kumpha' \
                    && echo 'glpat-f4dTxzyDBemNLeNr8MZj' \
                    && echo '123456' | sudo -S docker build -t registry.gitlab.com/Kumpha/jenkins-api-unittest . \
                    && echo '123456' | sudo -S docker push registry.gitlab.com/Kumpha/jenkins-api-unittest"
                    )

                }
            }
        }
        stage('Deploy on Vm3') {
            steps {
                echo 'gitlab pull and create container'
                sshCommand(remote: vm3, command: "echo '123456' | sudo -S docker login registry.gitlab.com \
                    && echo 'Kumpha' \
                    && echo 'glpat-f4dTxzyDBemNLeNr8MZj' \
                    && echo '123456' | sudo -S docker pull registry.gitlab.com/Kumpha/jenkins-api-unittest \
                    && echo '123456' | sudo -S docker stop api \
                    && echo '123456' | sudo -S docker rm api \
                    && echo '123456' | sudo -S docker run -d -p 8001:5000 --name api registry.gitlab.com/Kumpha/jenkins-api-unittest"
                    )

            }
        }
    }
}