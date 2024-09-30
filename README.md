BUGS:
 Issue getting the built package to install in new venv. PYTHONPATH env var is not set


This package can be used in all projects that connect to my raspberry pi server.

Package installation:
First, update the path to this repository in setup.py
Add the private_key, host_key, and config.json to project path that is importing this 
Inside your venv, run: pip install \path\to\package\.

setup.py will automatically add the package to your venv as an environment variable under PYTHONPATH
It will also install dependencies 
Then import sftp_pi