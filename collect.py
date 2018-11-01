import copy
import os
import re
import shutil

from wox import Wox, WoxAPI

AIM_PATH = r'C:\Users\Zero\Pictures\舔图猫'
RAW_PATH = r'C:\Users\Zero\AppData\Local\Packages\55370laplamgor.PRPR_z94bv1n74kjxt\LocalState'

RESULT_TEMPLATE = {
    'Title': '',
    'SubTitle': '',
    'IcoPath': 'Images/favicon.png',
}

ACTION_TEMPLATE = {
    'JsonRPCAction': {
        'method': '',
        'parameters': [],
    }
}

reg = re.compile(r'^\d+?-original\.(png|jpg|jpeg)$', flags=re.I)


class Main(Wox):

    def query(self, param):
        """Wox dealing programm

        Arguments:
            param {str} -- Wox window key in parameter

        Returns:
            list -- Wox json list
        """

        result = []
        param = param.strip().lower()

        if param:
            if param in ('lock', 'lockscreen'):
                p = os.path.join(RAW_PATH, 'Lockscreen')
                self.collect(p)

                title = "Pictures are already collected."
                subtitle = 'Click to open the aim folder in window.'
                method = 'openFolder'
                result.append(
                    self.genaction(title, subtitle, method, AIM_PATH))

            elif param in('desk', 'desktop'):
                p = os.path.join(RAW_PATH, 'Wallpaper')
                self.collect(p)

                title = "Pictures are already collected."
                subtitle = 'Click to open the aim folder in window.'
                method = 'openFolder'
                result.append(
                    self.genaction(title, subtitle, method, AIM_PATH))

            else:
                title = "Try to key in right command."
                subtitle = "Such as 'lock' or 'desk', try again."
                result.append(self.genformat(title, subtitle))
        else:
            title = "Auto collect your desktop wallpaper."
            subtitle = "For desktop wallpaper key in 'desk', for lock screen wallpaper key in 'lock'"
            result.append(self.genformat(title, subtitle))

        return result

    @staticmethod
    def collect(path):
        """Move wallpaper from PRPR cache path to aim path.

        Arguments:
            path {str} -- PRPR cache path
        """

        for file in os.listdir(path):
            if reg.match(file):  # find the yande's pictures
                raw = os.path.join(path, file)
                aim = os.path.join(AIM_PATH, file)

                if not os.path.exists(aim):
                    # copy picture to aim path
                    shutil.copy(raw, aim)

    @staticmethod
    def genformat(title, subtitle=''):
        """Generate wox json data

        Arguments:
            title {str} -- as name

        Keyword Arguments:
            subtitle {str} -- additional information (default: {''})

        Returns:
            json -- wox json
        """

        time_format = copy.deepcopy(RESULT_TEMPLATE)
        time_format['Title'] = title
        time_format['SubTitle'] = subtitle

        return time_format

    @staticmethod
    def genaction(tit, subtit, method, actparam):
        """Generate wox json data with copy action

        Arguments:
            title {str} -- as name
            actparam {str} -- the paramter which need to copy

        Returns:
            json -- wox json
        """

        res = copy.deepcopy(RESULT_TEMPLATE)
        res['Title'] = tit
        res['SubTitle'] = subtit

        action = copy.deepcopy(ACTION_TEMPLATE)
        action['JsonRPCAction']['method'] = method
        action['JsonRPCAction']['parameters'] = [actparam]
        res.update(action)

        return res

    def openFolder(self, path):
        os.startfile(path)
        WoxAPI.change_query(path)


if __name__ == '__main__':
    Main()