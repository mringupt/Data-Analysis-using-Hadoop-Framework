#!/usr/bin/python2


import cgi
import commands

print "content-type: text/html"
print

imageName=cgi.FormContent()['imagename'][0]
cName=cgi.FormContent()['cname'][0]


if commands.getstatusoutput("sudo docker inspect {0}".format(cName))[0]  == 0:
	print "<h3>{} : this container name already exists</h3>".format(cName)

else:
	commands.getoutput("sudo docker run  -dit --name {0}  {1}".format(cName,imageName))
	print "<h3>{}: Container launched ..</h3>".format(cName)
	print "<a href='docker_manage.py'>click here to manage container</a>"





