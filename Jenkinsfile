pipeline {
  agent any
  stages {
    stage('Lint') {
      steps {
        script {
          pipeline {
            agent { docker { image 'codacy/codacy-pylint' } }
            stages {
              stage('build') {
                steps {
                  sh 'pyLint hello.py > pylint.log'
                  sh 'ls -al'
                }
              }
            }
          }
        }

      }
    }
  }
}