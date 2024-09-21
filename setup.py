import subprocess
import sys

from setuptools import setup
import os

if not os.environ['PYTHONPATH'] or 'PYTHONPATH' not in os.environ:
    os.environ['PYTHONPATH'] = "C:\\Users\\Andrew\\Code Projects\\sftp_pi\\sftp_pi\\"
elif "C:\\Users\\Andrew\\Code Projects\\sftp_pi\\sftp_pi\\" not in os.environ['PYTHONPATH']:
    os.environ['PYTHONPATH'] += "C:\\Users\\Andrew\\Code Projects\\sftp_pi\\sftp_pi\\"

subprocess.check_call([sys.executable, '-m', 'pip', 'install','-r', 'requirements.txt'])

setup(
    name='sftp_pi',
    version='0.1.0',
    author='Andrew Westermann',
    author_email='a.westermann.19@gmail.com',
    packages=['sftp_pi'],
    # scripts=[''],
    # url='',
    description='A module for connecting to my server',
    long_description=open('README.md').read(),
)

