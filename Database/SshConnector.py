import logging
from sshtunnel import SSHTunnelForwarder


class SshConnector(object):

    def __init__(self, ipAddress, username, password):
        self.sshTunnel = SSHTunnelForwarder(ssh_address_or_host=ipAddress,
                                            ssh_username=username, ssh_password=password,
                                            remote_bind_address=('127.0.0.1', 3306),
                                            local_bind_address=('127.0.0.1', 3306))

    def startTunneling(self):
        logging.info('Establishing tunnel')
        self.sshTunnel.start()
        logging.info('Tunnel established')

    def stopTunneling(self):
        logging.info('Stopping tunnel')
        self.sshTunnel.stop()
        logging.info('Tunnel stopped')



