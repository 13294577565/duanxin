#!/usr/bin/env python
#coding=utf-8
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def send_sms(phone,code):
    client = AcsClient('LTAI4Fby8T5SfQFaRq8X8VBS', 'k82VcXpZabjpp59BLjp1IKjojXAndD', 'cn-hangzhou')

    phone='15011367759'

    code = "{'code':%s}" % (code)
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "kimen")
    request.add_query_param('TemplateCode', "SMS_178990423")
    request.add_query_param('TemplateParam', code)

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding = 'utf-8'))

def get_code(n=6,alpha=True):
    s = ''
    for i in range(n):
        num = random.randint(0,9)
        if alpha:
            upper_alpha = chr(random.randint(65,90))
            lower_alpha = chr(random.randint(97,122))
            num = random.choice([num,upper_alpha,lower_alpha])
        s = s+str(num)
    return s

if __name__ == '__main__':
    send_sms('13294577565',get_code(6,False))
    print(get_code(6,False))
    print(get_code(6,True))
    # print()