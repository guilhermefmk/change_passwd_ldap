
import paramiko
from paramiko import SSHClient
user = str(input('Usuário: '))
senha= str(input("Senha: "))
novasenha= str(input("Nova senha: "))

client_valida_user=SSHClient()
client_valida_user.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client_valida_user.connect('172.16.112.139', 22, username=f'{user}', password=f'{senha}', timeout=5)
    eh_valido = True
except:
    eh_valido = False
client_valida_user.close()


if eh_valido:
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('172.16.112.139', 22, username='guilherme.cunha', password='Vetorial#2020', timeout=5)

    cmd = f"powershell -InputFormat none -OutputFormat TEXT ./Desktop/script.ps1 -user '{user}' -senha '{novasenha}'"
    stdin, stdout, stderr = client.exec_command(cmd)
            #  gets the result of the command execution, and the data returned is one list

    stdin.close()



    client.close()
else:
    print('Senha não eh válido')