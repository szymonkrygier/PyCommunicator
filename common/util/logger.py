# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
from datetime import datetime

class Logger:
    @staticmethod
    def log(message):
        print("[{0}] > {1}".format(datetime.now(), message))
