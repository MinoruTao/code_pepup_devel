import datetime
import time
import boto3
import os

#メール関連の変数
_from = 'tsae360@gmail.com' # fromは予約語で使えない
_to = ['utmu41469@mineo.jp'] #配列
_subject = 'Subject: lambda_headless_pepup'
_body = 'Body: success'

def ses_send_email(_from, _to, _subject, _body):
    _ses = boto3.client('ses', region_name='us-west-2')
    _response = _ses.send_email(
        Source=_from,
        Destination={'ToAddresses': _to},
        Message={
            'Subject':{
                'Data': _subject,
            },
            'Body': {
                'Text': {
                    'Data': _body,
                },
            }
        }
    )

    return _response

ses_send_email(_from, _to, _subject, _body)
