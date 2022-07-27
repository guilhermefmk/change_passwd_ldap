
import paramiko
from paramiko import SSHClient
user = 'guilherme.cunha'
senha= 'Vetorial#20'



client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('172.16.112.139', 22, username='guilherme.cunha', password='Vetorial1223', timeout=5)

cmd = "powershell -InputFormat none -OutputFormat TEXT ./Desktop/script.ps1"
stdin, stdout, stderr = client.exec_command(cmd)
        #  gets the result of the command execution, and the data returned is one list

stdin.close()



client.close()