#/!/bin/bash
#Testing bash scripting
#Add dependencies that debian didn't natively have
apt-get install dirmngr
apt-get install git
apt-get install software-properties-common
add-apt-repository ppa:webupd8team/java
apt-get update
#Install jdk8 for Tron Compatabillity
apt-get install oracle-java8-installer

