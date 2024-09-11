import pysftp
import paramiko
from base64 import decodebytes
import json


class Connection (dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __init__(self, config_path, hostkey_path, private_key_path):
        super().__init__()
        config = json.loads(open(config_path).read())
        self['host'] = config['Host']
        self['user'] = config['User']
        self['port'] = config['Port']
        self['host key'] = open(hostkey_path).read()
        self['host key'] = str.encode(self['host key'])
        self['host key'] = paramiko.RSAKey(data=decodebytes(self['host key']))
        self['cnopts'] = pysftp.CnOpts(knownhosts=None)
        self['cnopts'].hostkeys.add(self['host'], 'ssh-rsa', self['host key'])

    def connect(self) -> pysftp.Connection:
        return pysftp.Connection(self['host'], username=self['user'], private_key='../private_key.ppk',
                               port=self['port'], cnopts=self['cnopts'])

    def test_connection(self):
        conn = self.connect()
        print(conn.execute('ls'))


# c = Connection('../config.json', '../hostkey.ppk', '../private_key.ppk')
# c.test_connection()
