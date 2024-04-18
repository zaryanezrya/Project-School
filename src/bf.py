from abc import ABC, abstractmethod
from typing import Dict

class IRAM(ABC):
    @abstractmethod
    def write(self, pointer: int, value: int) -> None:
        ...
    
    @abstractmethod
    def read(self, pointer: int) -> int:
        ...

class ICommand(ABC):
    @abstractmethod
    def execute(self):
        ...

class SimpleRAM(IRAM):
    def __init__(self, initial: Dict = None) -> None:
        if initial:
            self.memory = initial
        else:
            self.memory = {}

    def write(self, pointer: int, value: int) -> None:
        self.memory[pointer] = value
    
    def read(self, pointer: int) -> int:
        if pointer not in self.memory.keys():
            self.memory[pointer] = 0
        return self.memory[pointer]
    

class BFProcessor:
    def __init__(self, commands: Dict, program: IRAM, data: IRAM):
        self.commands = commands
        self.program = program
        self.data = data

        self.ip = 0
        self.dp = 0

        self.stack = []
        self.state = 'running'
    
    def process(self):
        while self.state == 'running':
            cmd = self._get_next_command()
            cmd.execute()
            self.ip += 1
    
    def _get_next_command(self) -> ICommand:
        current_operation = self.program.read(self.ip)
        return self.commands[current_operation](self)


class BFIncrementCommand(ICommand):
    def __init__(self, processor: BFProcessor) -> None:
        self.processor = processor

    def execute(self):
        dp = self.processor.dp
        current_value = self.processor.data.read(dp)
        self.processor.data.write(dp, current_value+1)

class BFDecrementCommand(ICommand):
    def __init__(self, processor: BFProcessor) -> None:
        self.processor = processor

    def execute(self):
        dp = self.processor.dp
        current_value = self.processor.data.read(dp)
        self.processor.data.write(dp, current_value-1)

class BFStopCommand(ICommand):
    def __init__(self, processor: BFProcessor) -> None:
        self.processor = processor
    
    def execute(self):
        self.processor.state = "stopped"

class BFPrintCommand(ICommand):
  def __init__(self, processor: BFProcessor):
    self.processor = processor
  
  def execute(self):
    data = self.processor.data
    dp = self.processor.dp
    print(data.read(dp))

class BFPrintCharCommand(ICommand):
  def __init__(self, processor: BFProcessor):
    self.processor = processor
  
  def execute(self):
    data = self.processor.data
    dp = self.processor.dp
    print(chr(data.read(dp)))


class BFRightCommand(ICommand):
  def __init__(self, processor: BFProcessor):
    self.processor = processor

  def execute(self):
    self.processor.dp += 1

class BFLeftCommand(ICommand):
  def __init__(self, processor: BFProcessor):
    self.processor = processor

  def execute(self):
    self.processor.dp -= 1


class BFStartLoopCommand(ICommand):
    def __init__(self, processor: BFProcessor):
      self.processor = processor
    
    def execute(self):
      dp = self.processor.dp
      data = self.processor.data
      if data.read(dp) == 0:
        while self.processor.program.read(self.processor.ip) != ']':
          self.processor.ip += 1
        return

      self.processor.stack.append(self.processor.ip)

class BFEndLoopCommand(ICommand):
    def __init__(self, processor: BFProcessor):
      self.processor = processor
    
    def execute(self):
      ip = self.processor.stack.pop()
      self.processor.ip = ip - 1