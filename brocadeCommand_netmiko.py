from netmiko import ConnectHandler
brocade = {
	'device_type':'brocade_vdx',
	'ip':'10.64.20.216',
	'username':'admin',
	'password':'password',
	}
net_connect = ConnectHandler(**brocade)
net_connect.find_prompt()
print net_connect.send_command("cfgshow")
print net_connect.send_command("version")


