*** Activate Virtual Env
    source venv/bin/activate    
*** Install pytest
    pip3 install pytest
*** Re-activate Virtual Env
    deactivate && source venv/bin/activate

** Start From Here

*** Install all dependencies into the virtual environment
    pip3 install -r requirements.txt
*** Run pytest
    python3 -m pytest
