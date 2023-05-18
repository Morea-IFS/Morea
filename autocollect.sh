#!bin/bash
date
. /home/production/Morea/env/bin/activate
python3 /home/production/Morea/manage.py collectstatic
deactivate