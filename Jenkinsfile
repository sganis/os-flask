pipeline {
  agent {
      label 'python'
  }
  stages {
    stage('Test') {
      steps {
        sh "pytest"
      }
    }
  }
}