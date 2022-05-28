import requests
import subprocess
import os
import logging
import notify
from datetime import datetime

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                        filename="/var/log/syncdir/syncdir.log", filemode="a")

def get_ips():
    ip_list = []
    with open("/home/shakir/ips", "r") as f:
        for line in f:
            ip_list.append(str(line).strip())
    return ip_list


if __name__ == "__main__":

    current_ip = requests.get('https://ifconfig.me').text

    ip_list = get_ips()

    vpn_ip = ip_list[0]
    base_ip = ip_list[1]

    print(current_ip, base_ip, vpn_ip)

    if current_ip == base_ip:
        # subprocess.run(["shutdown"])
        print('sudo shutdown now')
        if DISCORD_WEBHOOK:
            notify.shutting_down(webhook_url=DISCORD_WEBHOOK, ip_address=current_ip)

