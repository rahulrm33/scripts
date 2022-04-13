# Python Script to ping servers and alert via Mobile Phone when your server is down 

#### This scripts helps in monitoring your site irrespective to whether your computer is logged in or not and show an alert message when the site is down .

## Installation Steps 
### Sinch configuration 
###### Create a new account in sinch.com .
###### Try to copy authenticate token key and secret key.
### Script initialization
###### Fork this repository
###### Create a new virtual environment for python execution by command => virtualenv myenv
###### Install all dependences with command => 1. pip install requests 2. pip install sinchsms
###### With all the required information including mobile number , token id, secret key are given , notify which site to be get pinged in appropriate variable .  
##### In order to execute them alive make the script to run in Task scheduler which continuously execute the script. 
