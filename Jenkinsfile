pipeline {
  agent any
  stages {
    stage('Checkout'){ steps { checkout scm } }
    stage('Setup'){ steps { sh 'python -m pip install -r requirements.txt' } }
    stage('Test'){ steps { sh 'pytest -q' } }
    stage('Build'){ steps { sh 'docker build -t capgemini-rt-ml-platform:$BUILD_NUMBER .' } }
  }
}
