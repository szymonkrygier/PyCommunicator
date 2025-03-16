# PyCommunicator
# Copyright (C) 2022-2025 Szymon Krygier <szymon.krygier@pulsax.pl>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys

import importlib.util

# Sprawdzenie wersji Pythona
if sys.version_info < (3, 9, 7):
    print("Twoja wersja Pythona ({0}) nie jest wspierana przez aplikacje. Wymagana jest co najmniej wersja 3.9.7.".
          format(sys.version))
    exit(1)

# Sprawdzenie czy wymagane moduly sa dostepne
requiredModules = ['socket', 'PySide6', 'threading', 'array', 'dataclasses',
                   'datetime', 'signal', 'typing', 'Crypto', 'base64']

for module in requiredModules:
    if not module in sys.modules and importlib.util.find_spec(module) is None:
        print("Wymagany modul {0} nie zostal znaleziony! Aplikacja zostanie zaknieta.".format(module))
        exit(1)
