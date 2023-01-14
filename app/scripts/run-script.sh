#!

source /home/will/app/venv/bin/activate
nohup python /home/will/app/app/scripts/gather.py >> /home/will/app/app/scripts/gather.log &
ps -fA | grep /home/will/app/app/scripts/gather.py >> gather-pid.log
