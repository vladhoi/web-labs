#!/usr/bin/python3

import cgi
import os
import http.cookies


cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counter = cookie.get("submit_counter").value\
    if cookie.get("submit_counter") else 0

counter += 1

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

choice = form.getvalue('choice') if form.getvalue('choice')\
    else "Not set"

subjects = ','.join(form.getlist('subject'))

print("Content-type: text/html")
print()
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Form</title>
        </head>
<body>""")
print()
print("<h1>Form Processed</h1>")
print("<p>First name: {}</p>".format(first_name))
print("<p>Last name: {}</p>".format(last_name))
print("<p>Yes/no: {}</p>".format(choice))
print("<p>Subjects: {}</p>".format(subjects))
print("Times submitted <b>{}</b> times by you".format(counter))
print("<a href='http://localhost:8000'>Back to form</p>")
print("""</body>
</html>""")
