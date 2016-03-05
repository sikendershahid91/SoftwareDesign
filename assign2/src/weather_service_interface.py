import abc


class ZipcodeServiceInterface:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_zipcode_location(self, zipcode):
        raise NotImplemented

    @abc.abstractmethod
    def get_zipcode_weather(self, zipcode):
        raise NotImplemented
