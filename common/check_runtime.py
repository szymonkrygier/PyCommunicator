# Komunikator P2P z centralnym serwerem
# Szymon Krygier WCY19IJ1N1
import sys
import importlib.util

# Sprawdzenie wersji Pythona
if sys.version_info < (3, 9, 7):
    print("Twoja wersja Pythona ({0}) nie jest wspierana przez aplikacje. Wymagana jest co najmniej wersja 3.9.7.".format(sys.version))
    exit(1)

# Sprawdzenie czy wymagane moduly sa dostepne
requiredModules = ['socket', 'PySide6', 'threading', 'array', 'dataclasses', 'datetime', 'signal']

for module in requiredModules:
    if not module in sys.modules and importlib.util.find_spec(module) == None:
        print("Wymagany modul {0} nie zostal znaleziony! Aplikacja zostanie zaknieta.".format(module))
        exit(1)
