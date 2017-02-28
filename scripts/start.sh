source ~/.yosenv/bin/activate

cd /yosbot
pip install -r requirements.txt

nohup rtmbot &>/dev/null &
