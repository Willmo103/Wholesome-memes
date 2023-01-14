#!

source /home/will/app/venv/bin/activate
nohup python /home/will/app/src/app/scripts/gather.py >> /home/will/app/src/app/scripts/gather.log &
ps -fA | grep /home/will/app/src/app/scripts/gather.py >> gather-pid.log
