#!

source /home/will/app/venv/bin/activate
python /home/will/app/app/scripts/gather.py >> /home/will/app/app/scripts/gather.log
echo "---" >> /home/will/app/app/scripts/gather.log
deactivate

# cronjob this script (*/0,*/30 * * * * )
