import time
import typing
from colorama import Fore, init, Style

init(autoreset=True)

_merah = Fore.LIGHTRED_EX
_hijau = Fore.LIGHTGREEN_EX
_kuning = Fore.LIGHTYELLOW_EX
_magenta = Fore.LIGHTMAGENTA_EX
_biru = Fore.LIGHTBLUE_EX
_reset = Style.RESET_ALL
_putih = Fore.LIGHTWHITE_EX
_cyan = Fore.LIGHTCYAN_EX


class Log:
    def __init__(self):
        pass

    def get_time(self):
        year, mon, day, hour, minute, second, wd, yd, dst = time.localtime()
        data = (
            str(year)
            + "-"
            + str(mon).zfill(2)
            + "-"
            + str(day).zfill(2)
            + " "
            + str(hour).zfill(2)
            + ":"
            + str(minute).zfill(2)
            + ":"
            + str(second).zfill(2)
        )
        return data

    @staticmethod
    def success(text: typing.Any):
        l = Log()
        print(f"{_biru}[{l.get_time()}]{_putih} -{_reset} {_hijau}{text} ")

    @staticmethod
    def warn(text: typing.Any):
        l = Log()
        print(f"{_biru}[{l.get_time()}]{_putih} -{_reset} {_kuning}{text} ")

    @staticmethod
    def error(text: typing.Any):
        l = Log()
        print(f"{_biru}[{l.get_time()}]{_putih} -{_reset} {_merah}{text} ")

    @staticmethod
    def write(file: str = "app.log", text: typing.Any = ""):
        l = Log()
        data = f"[{l.get_time()}] - {text}\n"
        open(file=file, mode="a+", encoding="utf-8").write(data)

    @staticmethod
    def countdown(t: int):
        """
        t: int, how many second !
        """
        lo = "☉ "
        co = 1
        while t:
            minute, second = divmod(t, 60)
            hour,minute = divmod(minute, 60)
            _format = (
                str(hour).zfill(2)
                + ":"
                + str(minute).zfill(2)
                + ":"
                + str(second).zfill(2)
            )
            print(f"{_kuning}wait {_format} {lo * co} ",flush=True,end='\r')
            if co == 6:
                co = 1
                print('                         ',flush=True,end='\r')
                continue
            
            co += 1
            t -= 1
            time.sleep(1)

