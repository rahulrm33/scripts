# Python Script to ping servers and alert via Mobile Phone when your server is down 

#### This scripts helps in monitoring your site irrespective to whether your computer is logged in or not and show an alert message to your mobile phone when the site is down .

## Installation Steps 
### Sinch configuration 
1. Create a new account in sinch.com .
2. Try to generate your own authenticate token key and secret key.
### Script initialization
1. Create a new virtual environment for python execution by command => virtualenv myenv
2. Move to that environment by command => cd myenv
3. Install all dependences with command => 1. pip install requests 2. pip install sinchsms
4. Fork this repository.
5. Add all the required information . 
6. With all the required information including mobile number , token id, secret key are given , notify which site to be get pinged in script file .  
##### In order to execute them alive make the script to run in Task scheduler which continuously execute the script. 
