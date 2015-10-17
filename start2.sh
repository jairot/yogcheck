#!/bin/bash
 
NAME="yogcheck" # Name of the application
DJANGODIR=/home/azureuser/yogcheck/ # Django project directory
USER=azureuser  #the user to run as
GROUP=azureuser
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
#DJANGO_SETTINGS_MODULE=settings # which settings file should Django use
 
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $DJANGODIR
source bin/activate
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
 
# Create the run directory if it doesn't exist
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec bin/gunicorn \
-b 127.0.0.1:4000 \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=debug hello:app

