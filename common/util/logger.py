# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from datetime import datetime


class Logger:
    @staticmethod
    def log(message):
        now = datetime.now()

        print("[{0}] > {1}".format(now.strftime("%Y-%m-%d %H:%M"), message))
