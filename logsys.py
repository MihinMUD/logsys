from datetime import datetime
class __Logsys:
    def __init__(self, log, TimeStamp=False):
        self.log = log
        self.TimeStamp = TimeStamp
    def __dataF(self,term):
        time = datetime.now().strftime('%H:%M:%S')
        if self.TimeStamp:
            return f"[{self.log}] {term} - {time}"
        else:
            return f"[{self.log}] {term}"

    def logConsole(self,term):
        print(self.__dataF(term))


    def logFile(self, path,  term):
        data = self.__dataF(term)
        try:
            file = open(path , 'r+')
        except FileNotFoundError:
            file = open(path , 'w')
        finally:
            file = open(path , 'r+')
            content = file.read()
            file.seek(0, 0)
            file.write(data.rstrip('\r\n') + '\n' + content)
            file.close()

log = __Logsys
