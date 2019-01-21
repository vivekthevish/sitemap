# sitemap

Author = 'Vivek Sharma'

Program Description:
'''
This program will take a website name as input and list out all the links on the given page.
It will then go to each links on the listed pages and list out all the links on the respective pages.
The program will end once it traverse all the links on the main page.'''


To run the program:
Go to the program folder on the terminal and Install requirements.txt with below command
>> pip install -r requirements.txt
 
 
 Run the program with the below command
>> python sitemap.py https://www.domain_name.com

Note:
1. The Link given should be in the format "http://domain_name.com" or "http://www.domain_name.com"
   I have attached a sample run file 'log.txt'
2. This program will not able to crawl through few websites such as "https://www.hdfc.com" 
   may be due to security reasons of the website.
3. The output will only be showing up on the terminal.
   If you wish to capture the logs in a separate file please run the script in below format
>> python sitemap.py https://www.domain_name.com > log.txt
