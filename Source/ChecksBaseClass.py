from abc import ABC, abstractmethod
from typing import List


class NotImplementedError(Exception):
    pass


class ItemToCheck(ABC):
    """
    A class that represents a single check that can be performed to check the health of a 
    system or process. Methods and attribute setters must be defined in any subclasses. 
    If subclasses attempt to call non-implemented methods in this base class it will
    raise a 'NotImplementedError' exception.

    Attributes
    ----------
    process_name : str
    help_text : str
    is_healthy : bool
    error_data : List[str]
    url : str

    Methods
    -------
    _perform_check(self) -> bool:
        Sets the attributes 'error_data' and 'is_healthy'. Should be called in the subclass'
        __init__() function definition.
    
    help_text(self) -> str:
        Returns the string help text displayed when a consumer of the class wants more info
        about the health check.

    error_data(self) -> List[str]:
        Returns a list of strings that contain information about the health check. This can be
        a list of each item causing an error or a list with a single string that describes
        what caused the error.

    process_name(self) -> str:
        Returns the string that contains the name of the process or system being checked.

    is_healthy(self) -> bool:
        Returns the string help text displayed when a consumer of the class wants more info
        about the health check. 

    url(self) -> str:
        Returns a URL related to the check.
    """

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def _perform_check(self) -> bool:
        """Actually performs the health check on the system/process."""
        raise NotImplementedError

    @property
    @abstractmethod
    def error_data(self) -> List[str]:
        """Contains data about the error. Exampels are a list of dates missing data or an 
        error message from the system. Should be an empty list if no errors are detected"""
        raise NotImplementedError

    @error_data.setter
    def error_data(self, val):
        raise NotImplementedError

    @error_data.deleter
    def error_data(self, val):
        raise NotImplementedError

    @property
    @abstractmethod
    def url(self) -> List[str]:
        """Contains a url related to the check."""
        raise NotImplementedError

    @url.deleter
    def url(self, val):
        raise NotImplementedError

    @property
    @abstractmethod
    def is_healthy(self) -> bool:
        """Checks the health of a system or process. Returns True if healthy."""
        raise NotImplementedError

    @is_healthy.setter
    def is_healthy(self, val):
        raise NotImplementedError
    
    @is_healthy.deleter
    def is_healthy(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def process_name(self) -> str:
        """Provides the name of the process"""
        raise NotImplementedError

    @process_name.setter
    def process_name(self, val):
        raise NotImplementedError

    @process_name.deleter
    def process_name(self) -> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def help_text(self) -> str:
        """Provides help text that describes what the output means and when it may be expected to fail."""
        raise NotImplementedError
    
    @help_text.setter
    def help_text(self) -> None:
        raise NotImplementedError

    @help_text.deleter
    def help_text(self) -> None:
        raise NotImplementedError

    def __str__(self):
        return f"""process_name: {self.process_name};

help_text: {self.help_text}; 
is_healthy: {self.is_healthy}; 
error_data: {str(self.error_data)}"""


if __name__ == '__main__':
    raise Exception("This script is not meant to be called directly. Perhaps you meant to run ChecksController.py?")
