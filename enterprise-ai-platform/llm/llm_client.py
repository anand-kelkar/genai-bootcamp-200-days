# This is parent class to call the LLM and return response
from abc import ABC, abstractmethod

class LLMClient(ABC):
    @abstractmethod
    def generate(self,prompt):
        pass

