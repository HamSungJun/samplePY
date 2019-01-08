pipeline{
   agent any
   stages{
       stage('clone'){
           steps{
               git 'https://github.com/HamSungJun/samplePY.git'
           }
       }
       stage('build'){
           steps{
              sh "#!/bin/bash && \

                  echo 'Constructing ($2) virtual python environment with version ($1)...' && \

                  reportPath='QualityReports' && \
                  Mdepth=`find . -type d -printf '%d\n' | sort -rn | head -1` && \
                  source ~/.bash_profile && \

                  pyenv install -s $1 && \

                  pyenv virtualenv $1 $2 && \

                  source activate $2 && \

                  pip install --upgrade pip && \

                  pip install -r requirements.txt && \

                  pip install pylint coverage unittest-xml-reporting && \

                  if [ -d '$reportPath' ] && \
                  then && \
                      rm -rf '$reportPath' && \
                      mkdir '$reportPath' && \
                  else && \
                      mkdir '$reportPath' && \
                  fi && \

                  python3 -m pylint --generate-rcfile > pylint.cfg && \
                  python3 -m pylint --rcfile=pylint.cfg $(find . -maxdepth '$Mdepth' -name '*.py') --msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}' --disable=C0111,C0103,E0602,W0612,W0702,R0801 > ./QualityReports/pylint.log"
           }
       }
   }
   post {
        always {
            echo 'I will always say Hello again!'
        }
   }
}
