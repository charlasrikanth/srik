# srik
#Log analysis project

-To create a reporting tool that prints out reports (in plain text) based on the data in the database.

#Project purpose

To write SQL queries to answer the following questions.
-What are the most popular three articles of all time?
-Who are the most popular article authors of all time?
-On which days did more than 1% of requests lead to errors?

#Run the project

-Download the project zip file to your computer and unzip the file.
-Open the text-based interface for your operating system and navigate to the project directory.
-Bring up the VM with the following command:
 vagrant up
-You can then log into the VM with the following command:
 vagrant ssh
 
#Load the logs into the database

First, unzip the zip file.
Then run the following command to load the logs into the database:
psql -d news -f newsdata.sql

#Run the reporting tool

-The logs reporting tool is executed with the following command:
 python3 logs_analysis_tool.py
-The answers to the three questions should now be displayed.

#Shutting the VM down
-When you are finished with the VM, shut it down.
 vagrant halt

