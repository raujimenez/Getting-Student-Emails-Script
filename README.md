# What is this?

Since some teachers do not allow us to mass email other students on canvas because they have the options disabled. I decided to create a script that would allow me approximately get the list of all emails for the students in the course number. 

This program DOES NOT send the email for you. You still have to create the group me. All this program does is give you the emails so you can copy and paste.

This only give the approximate emails of the students. If they have numbers in their student email, sucks to be them. 


## Pre-requisites
-Have python installed. You can install it on [https://www.python.org/](https://www.python.org/). Just make sure you download python 3.xx or later.


# Getting Started

 - First you are going to want to get a copy of the python script. Type this into your terminal 
	 - `git clone https://github.com/raujimenez/Getting-Student-Emails-Script.git`
	- Alternatively you can just download the zip
- Once the files are downloaded go into the folder where you download the files
- Run the python script:
	-  Windows: `python email_generation.py` 
	- Linux/Mac: `python3 email_generation.py` 

## What is my course number?
You can see a course number in the URL of the course you want to see. 
 1. Go to [https://uta.instructure.com/](https://uta.instructure.com/) and login
 2. Click on the course you want to get the emails of students with
 3. Now the URL Bar should look like this 
	- `https://uta.instructure.com/courses/<COURSE NUMBER>`
4.  Get this course number and place into the console application

## How do I get a token?

Since the python script does not save your token in a cookie like a browser does you need to generate one that will be specific to the script. Don't worry this one is easy!
1. Login into canvas
2. Click on `Accounts` on the left hand side
3. Click on `Settings`
4. Scroll down until you see the blue button that says `+ New Access Token` and click on it
5. Name it anything and generate the token. You can leave the expiration date blank if you want.
6. Copy the token and paste it into the prompt when requested.

## Notes
I created this in windows so I can only gurantee that it functions in windows. If you have a Mac or a Linux machine you can shoot me an email or go on a google expedetion. 

**IMPORTANT**
I do realize that this will not work if the student has a number after their name, this is to approximate.

Hopefully someone will send them the link to the group me.