import abc


class ZipcodeServiceInterface: #Venkat: Too much here. In reality we don't need this at all. Python is quite dynamic, it does not need defining interfaces or abstract classes. We can remove this.
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_zipcode_location(self, zipcode):
        raise NotImplemented

    @abc.abstractmethod
    def get_zipcode_weather(self, zipcode):
        raise NotImplemented
