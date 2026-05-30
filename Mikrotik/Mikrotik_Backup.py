from netmiko.mikrotik.mikrotik_ssh import MikrotikRouterOsSSH
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from yaml import safe_load

with open('inventory.yaml', 'r', encoding='utf-8') as inventory:
    config = safe_load(inventory)

IPS = [device['ip'] for device in config['devices']]

USERNAME = config.get('credentials', {}).get('username')
PASSWORD = config.get('credentials', {}).get('password')
MAX_WORKERS = config.get('backup', {}).get('max_workers')

NODE = {
    'username': USERNAME,
    'password': PASSWORD
}

def backup(ip):
    device = NODE.copy()
    device['host'] = ip

    connection = MikrotikRouterOsSSH(**device)

    identity = connection.send_command('/system identity print').split()[1]
    output_csr = connection.send_command('/export show-sensitive')

    filename = f"{identity}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.rsc"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(output_csr)

    connection.disconnect()

with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
    ex.map(backup, IPS)