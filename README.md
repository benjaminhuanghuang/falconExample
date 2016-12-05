* Reference
    Python Falcon Tutorial
    
* Setup for Python 3.5
** Step 1: install python 3.5
    $brew install python3

    python3 --version
    Python 3.5.2

** Step 2: install virtaul machine:
    pyvenv venv3

** Step 3: start your python 3 virtaul machine:
    source venv3/bin/activate

** Step 4: install python package in your python 3 virtul machine
    pip3 install  -r requirements.txt

** Step 5: stat your python flacon server:
    uwsgi --http :8000 --wsgi-file run.py --callable app --enable-threads  --thunder-lock
