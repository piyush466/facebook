import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class Readconfig:
    @staticmethod
    def getApplicationURL():
        Url = config.get("common info","baseUrl")
        return Url

    @staticmethod
    def getusernamee():
        username = config.get("common info","username")
        return username

    @staticmethod
    def get_password():
        password =config.get("common info","password")
        return password
