import winrm

s = winrm.Session('192.168.60.151', auth=('Administrator', 'vagrant'))
r = s.run_cmd('ipconfig', ['/all'])
