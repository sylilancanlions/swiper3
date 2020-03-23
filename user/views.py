from django.shortcuts import render


# Create your views here.
from user.logic import send_verify_code
from lib.http import render_json



def get_verify_code(request):
    """phone register"""
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None,0)



def login(request):
    """message verify to login"""
    pass


def get_progile(request):

    pass

def modify_profile(request):
    pass

def upload_avatar(request):
    pass
