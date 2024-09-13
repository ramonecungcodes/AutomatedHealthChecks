import ChecksBaseClass as ChecksBaseClass
from typing import List

class ExampleHealthyProcessName(ChecksBaseClass.ItemToCheck):
    def __init__(self):
        self.__process_name = "My Example Healthy Process"
        self.__help_text = "This example is manually set. Update the function ExampleHealthyProcessName._perform_check() to return True or False if you need different data." 
        self.__error_data = []
        self.__is_healthy = self._perform_check()
        self.__url = ""

    @property
    def process_name(self) -> str:
        return self.__process_name

    @process_name.setter    
    def process_name(self, val) -> None:
        pass

    @property
    def help_text(self) -> str:
        return self.__help_text
    
    @help_text.setter
    def help_text(self, val) -> None:
        pass


    @property
    def is_healthy(self) -> str:
        return self.__is_healthy
    
    @is_healthy.setter
    def is_healthy(self, val) -> None:
        pass


    @property
    def error_data(self) -> List[str]:
        return self.__error_data
    
    @error_data.setter
    def error_data(self, val) -> None:
        pass


    @property
    def url(self) -> List[str]:
        return self.__url
    
    @url.setter
    def url(self, val) -> None:
        pass


    def _perform_check(self) -> bool:
        """Returns test data to test abstract base class CheckBaseClass.ItemToCheck"""
        
        result = True
        
        if result:
            return True
        else:
            self.__error_data = ["2024-05-01", "2024-06-09"]
            return False


class ExampleFaultedProcessName(ChecksBaseClass.ItemToCheck):
    def __init__(self):
        self.__process_name = "My Example Faulted Process"
        self.__help_text = "This example is manually set. Update the function ExampleFaultedProcessName._perform_check() to return True or False if you need different data." 
        self.__error_data = []
        self.__is_healthy = self._perform_check()
        self.__url = ""

    @property
    def process_name(self) -> str:
        return self.__process_name

    @process_name.setter    
    def process_name(self, val) -> None:
        pass


    @property
    def help_text(self) -> str:
        return self.__help_text
    
    @help_text.setter
    def help_text(self, val) -> None:
        pass

    @property
    def is_healthy(self) -> str:
        return self.__is_healthy
    
    @is_healthy.setter
    def is_healthy(self, val) -> None:
        pass

    @property
    def error_data(self) -> List[str]:
        return self.__error_data
    
    @error_data.setter
    def error_data(self, val) -> None:
        pass

    @property
    def url(self) -> List[str]:
        return self.__url
    
    @url.setter
    def url(self, val) -> None:
        pass

    def _perform_check(self) -> bool:
        """Returns test data to test abstract base class CheckBaseClass.ItemToCheck"""
        
        result = False
        
        if result:
            return True
        else:
            self.__error_data = ["2024-05-01", "2024-06-09"]
            return False


# process_list = [ExampleHealthyProcessName, ExampleFaultedProcessName]
process_list = [ExampleHealthyProcessName, ExampleFaultedProcessName]

if __name__ == '__main__':
    raise Exception("This script is not meant to be called directly. Perhaps you meant to run ChecksController.py?")
