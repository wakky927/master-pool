#!/bin/bash

cd ../

python3 fugafuga.py "" "" 0 500 &
python3 fugafuga.py "" "" 500 1000 &
python3 fugafuga.py "" "" 1000 1500 &
python3 fugafuga.py "" "" 1500 2000 &
python3 fugafuga.py "" "" 2000 2500 &
python3 fugafuga.py "" "" 2500 3000 &
python3 fugafuga.py "" "" 3000 3500 &
python3 fugafuga.py "" "" 3500 3900 &

wait

python3 fugafuga.py "" "" 0 500 &
python3 fugafuga.py "" "" 500 1000 &
python3 fugafuga.py "" "" 1000 1500 &
python3 fugafuga.py "" "" 1500 2000 &
python3 fugafuga.py "" "" 2000 2500 &
python3 fugafuga.py "" "" 2500 3000 &
python3 fugafuga.py "" "" 3000 3500 &
python3 fugafuga.py "" "" 3500 3900 &

wait

echo "all program fin."