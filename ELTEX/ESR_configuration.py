from netmiko.eltex.eltex_esr_ssh import EltexEsrSSH

divice_template = {'device_type' : 'eltex_esr',
          'ip': '172.16.21.61',
          'username' : 'admin',
          'password' : '123',
          }

ssh = EltexEsrSSH(**divice_template)



#commands = ['username user101',
#            'privilege 15',
#            'password p@ssword1']

ssh.send_config_set('no user user101')

#ssh.send_config_set(commands)

ssh.commit()

ssh.send_command('confirm')

ssh.disconnect()