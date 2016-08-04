from subprocess import call
import os

HOME =  os.path.join("/usr/")
CURRENT =  os.path.join("/srv/www/code/endpoints/")
COMMAND = "uwsgi --http 0.0.0.0:8080 --home %s --chdir %s -w create:wsgi_app" %(HOME, CURRENT)

def main():
	call(COMMAND, shell=True)

if __name__ == "__main__":
    main()