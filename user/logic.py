import random

import requests
from django.core.cache import cache

from swiper3 import config
from worker import call_by_worker


def gen_verify_code(length = 6):
    return random.randrange(10**(length-1),10**length)


@call_by_worker
def send_verify_code(phonenum):
    vcode = gen_verify_code()
    key = 'VerifyCode-%s'%phonenum
    #使用缓存来记录验证码，第一二个参数是类似于字典的键值对，第三个参数是过期时间
    cache.set(key,vcode,120)
    sms_cfg = config.HY_SMS_PARAMS.copy()
    sms_cfg['content'] = sms_cfg['content']%vcode
    sms_cfg['mobile'] = phonenum
    response = requests.post(config.HY_SMS_URL,data = sms_cfg)
    return response