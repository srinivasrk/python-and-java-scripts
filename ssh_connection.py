import paramiko
ssh = paramiko.SSHClient()
output=""
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.241.216.224',username='nasadmin',password='nasadmin')

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('hostname')
stdout=ssh_stdout.readlines()
for line in stdout:
    output=output+line
if output!="":
    print output
else:
    print 'This is error =',ssh_stderr.readlines()
    print "There was no output for this command"

