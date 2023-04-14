import os
import pysnowball.cons as cons
token="xqat=758141a86b7a186c9dd0b7840ed65c779e1dacf3;"
    
def get_token():
    # return '123'
    # if os.environ.get('XUEQIUTOKEN') is None:
    #     raise Exception(cons.NOTOKEN_ERROR_MSG)
    # else:
    #     return os.environ['XUEQIUTOKEN']
    print("if occur some error,cookie may wrong")
    return ''.join(token)

def set_token(token):
    os.environ['XUEQIUTOKEN'] = token
    return os.environ['XUEQIUTOKEN']
