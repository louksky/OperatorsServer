from api_eng_.operators import RegisteredOperatorsEngine


class APISettings:
    """
    Class holds settings for all api_eng_ project
    """
    regi = RegisteredOperatorsEngine()
    #copyrights = 'Asaf Louk (skywalker)'
    __copyrights__ = 'Asaf Louk (skywalker)'


local_settings = APISettings()
