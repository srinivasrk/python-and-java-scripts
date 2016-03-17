import paramiko
import time
client = paramiko.SSHClient() 
client.load_system_host_keys() 
client.set_missing_host_key_policy(paramiko.WarningPolicy()) 
print '*** Connecting...' 
client.connect('10.241.216.224', username='nasadmin', password='nasadmin') 


channel1 = client.invoke_shell()
channel1.send('nas_server -list -all \n')
time.sleep(3)
stdout=""
while channel1.recv_ready():
        stdout += channel1.recv(1024)
        
print(stdout)

channel1.send('nas_cel -list \n')
time.sleep(3)
while channel1.recv_ready():
    stdout += channel1.recv(1024)
print(stdout)

client.close()
