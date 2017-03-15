import sys
import paramiko 

address = sys.argv[1]
port = int(sys.argv[2])
name = sys.argv[3]
path = sys.argv[4]
prefix = sys.argv[5]
counts = int(sys.argv[6])
mode = sys.argv[7]
passwd = "kv020DevOps"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(address, port=port, username=name, password=passwd)
for i in range(1,counts):
    command = "mkdir -m" + mode + " /home/" + prefix + str(i)
    stdin, stdout, stderr = ssh.exec_command(command)

print stdout.read()

ssh.close()
