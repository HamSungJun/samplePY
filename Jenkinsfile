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
               sh 'reportPath="QualityReports" &&\
               Mdepth=`find . -type d -printf "%d\n" | sort -rn | head -1` && \
               . ~/.bash_profile && pyenv install -s 3.5.2 && \
               pyenv virtualenv 3.5.2 myenv && pyenv activate myenv && \
               pip install --upgrade pip && \
               pip install -r requirements.txt && \
               pip install pylint coverage unittest-xml-reporting && \
               rm -rf "$reportPath" && \
               mkdir "$reportPath" && \
               python3 -m pylint --generate-rcfile > pylint.cfg && \
               python3 -m pylint --rcfile=pylint.cfg $(find . -maxdepth "$Mdepth" -name "*.py") --disable=C0111,C0103,E0602,W0612,W0702,R0801 > ./QualityReports/pylint.log | exit 0'
           }
       }
   }
}