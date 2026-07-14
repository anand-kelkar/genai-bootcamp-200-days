# responsibility of this class is to parse LLM output and return JSON string
import json
from abc import ABC, abstractmethod

class OutputParser(ABC):
    @abstractmethod
    def parse(self,response):
        pass

