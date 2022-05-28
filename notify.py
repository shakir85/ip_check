import datetime
import logging
from http.client import HTTPException
from discord import Webhook, RequestsWebhookAdapter, Embed, NotFound, Forbidden

"""
colors:
    teal -> 0x1abc9c
    green -> 0x2ecc71
    red -> 0xe74c3c
"""

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename="/var/log/syncdir/syncdir.log", filemode="a")


def shutting_down(webhook_url, ip_address):
    """Sends a message to Discord with message border color == Red"""

    now = datetime.datetime.now()
    webhook = Webhook.from_url(webhook_url, adapter=RequestsWebhookAdapter())
    embed = Embed(timestamp=now.now(), tilte="rsync backup", description="[Alert] failed", color=0xe74c3c)
    try:
        webhook.send(embed=embed, content=f"IP address changed to [{ip_address}], server is going to shutdown now")
        logging.info("Success message sent to Discord channel")

        msg = webhook.send(embed=embed, content=f"Rsync backup failed for job {ip_address}")
        logging.info("Notification wes send to Discord successfully.")
        return msg

    except HTTPException as h:
        logging.error(f"Failed to send Discord message.\n{h}")
    except NotFound as nf:
        logging.error(f"Webhook is not found!\n{nf}")
    except Forbidden as fb:
        logging.error(f"Webhook authorization token is incorrect!\n{fb}")



