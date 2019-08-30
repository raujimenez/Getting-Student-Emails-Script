import requests
import json

#Created by Raul Jimenez, UTA CS Senior
"""
    Since some teachers do not allow us to mass email other students on canvas because they have the options disabled 
    I decided to create a script that would allow me approximatly get the list of all emails for the students in the course number

    If you guys want to extend the code please feel free, I just wanted to create it to create a groupme for CSE 3315

    NOTE: I do realize that this will not work if the student has a number after their name, this is to approximate.
    Hopefully someone will send them the link to the group me.

    for more information please visit the api for canvas
"""

course_id = input('Input the course id you see in the url of your canvas class. It will typically look like (https://uta.instructure.com/courses/<NUMBER YOU WANT>): ')

# I know that students is deprecated but I used it because users did not return the full class roster
URL = "https://uta.instructure.com/api/v1/courses/" + course_id + "/students"

# For more information on how to generate a token please see https://community.canvaslms.com/docs/DOC-10806-4214724194
token = input('input the token (this can be generated in the settings tab in the canvas profile): ')

r = requests.get(URL + "?access_token=" + token)
students = r.json()

for student in students:
    full_name = student['sortable_name']
    last_name, first_name = full_name.split(',') 
    
    last_name.strip()
    first_name.strip()   
    
    last_name = last_name.replace(" ", "")
    first_name = first_name.replace(" ", "")

    email = first_name.lower() + '.' + last_name.lower() + '@mavs.uta.edu'
    print(email)    