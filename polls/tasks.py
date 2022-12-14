from datetime import datetime


import requests
import json

from django.utils import timezone
from mailing.celery import app
from .models import Client, Mailing, Message
from django.shortcuts import get_object_or_404

@app.task
def send_verification_msg(mailing_id):
    mailing = Mailing.objects.get(id=mailing_id)
    clients = Client.objects.filter(tag=mailing.tag)
    datetime_now = timezone.now()
    keep_running = datetime_now > mailing.mailing_start and datetime_now < mailing.mailing_end
    if keep_running:
        msg = Message(msg_start=datetime_now, msg_status=0, id_mailing=mailing)
        try:
            for client in clients:
                msg.id_client = client.get('id')
                headers = {
                    "Authorization": '"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE2NjAyNTAsImlzcyI6ImZhYn'
                                     'JpcXVlIiwibmFtZSI6ImJvZ2Rhbl9rYyJ9.Kto44M36XLGa3bo22Aw23mQnEhIIEUqRmQqAjk8DJIQ"'
                }
                body = {
                    "id": msg.id,
                    "phone": client.get("phone"),
                    "text": mailing.msg_text
                }
                responce = requests.post(f"https://probe.fbrq.cloud/v1/send/{msg.id}", headers=headers,
                                         data=json.dumps(body))
                print(responce)
                msg.msg_status = 1
                client_id = client.id
                client = get_object_or_404(Client, pk=client_id)
                client.delete()
        except:
            msg.msg_status = 2
        msg.save()
