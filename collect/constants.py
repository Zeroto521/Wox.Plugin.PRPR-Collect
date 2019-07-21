# -*- coding: utf-8 -*-

from getpass import getuser

USERNAME = getuser()

AIM_PATH = r'C:\Users\{}\Pictures\舔图猫'.format(USERNAME)
RAW_PATH = r'C:\Users\{}\AppData\Local\Packages\55370laplamgor.PRPR_z94bv1n74kjxt\LocalState'.format(
    USERNAME)

RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'images/favicon.png',
}

ACTION_TEMPLATE = {
    'JsonRPCAction': {
        'method': '',
        'parameters': [],
    }
}
