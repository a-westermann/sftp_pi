import pysftp
import paramiko
from base64 import decodebytes
import json
import os


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
        self['private key path'] = private_key_path
        self['cnopts'] = pysftp.CnOpts(knownhosts=None)
        self['cnopts'].hostkeys.add(self['host'], 'ssh-rsa', self['host key'])
        self.connection = self.connect()

    def connect(self) -> pysftp.Connection:
        return pysftp.Connection(self['host'], username=self['user'],
                            private_key=self['private key path'], port=self['port'], cnopts=self['cnopts'])

    def test_connection(self):
        conn = self.connect()
        print(conn.execute('ls'))

    def upload_file(self, local_file_path, remote_path):
        self.connection.put(local_file_path, remote_path)

    def upload_dir(self, local_dir, remote_dir, dir_exclusions: [str], file_suffix_exclusions: [str]):
        for entry in os.listdir(local_dir):
            if local_dir.split('\\')[-1] in dir_exclusions:
                return
            remote_path = remote_dir + '/' + entry
            local_path = os.path.join(local_dir, entry)
            print(local_path)
            print(remote_path)
            if not os.path.isfile(local_path):
                try:
                    self.connection.mkdir(remote_path)
                except OSError:
                    pass
                self.upload_dir(local_path, remote_path, dir_exclusions, file_suffix_exclusions)
            elif len([x for x in file_suffix_exclusions if local_path.endswith(x)]) == 0:
                self.upload_file(local_path, remote_path)

    def download(self, remote_path, local_path):
        self.connection.get(remote_path, local_path)


# c = Connection('../config.json', '../hostkey.ppk', '../private_key.ppk')
# c.test_connection()
