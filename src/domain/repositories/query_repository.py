from abc import ABC, abstractmethod

class QueryRepository(ABC):
    @abstractmethod
    def run(self, sql: str):
        pass
