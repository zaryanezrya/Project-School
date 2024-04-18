import unittest

from src.bf import (
    SimpleRAM, BFProcessor, BFIncrementCommand, BFStopCommand, BFPrintCommand, BFPrintCharCommand,
    BFLeftCommand, BFRightCommand, BFStartLoopCommand, BFEndLoopCommand, BFDecrementCommand
)
    


class TestSimpleRAM(unittest.TestCase):
    def test_read_write_1(self):
        mem = SimpleRAM()

        mem.write(101, 42)
        val = mem.read(101)

        self.assertEqual(val, 42)
    
    def test_read_write_2(self):
        mem = SimpleRAM()

        val = mem.read(101)

        self.assertEqual(val, 0)


class TestBFProcessor(unittest.TestCase):

    def test_increment(self):
        commands = {
            "+": BFIncrementCommand,
            "-": BFDecrementCommand,
            ".": BFPrintCharCommand,
            "<": BFLeftCommand,
            ">": BFRightCommand,
            "[": BFStartLoopCommand,
            "]": BFEndLoopCommand,
            0: BFStopCommand,
        }
        # text = "+>++++<[->+<]>." # умножение
        text = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'
        program = SimpleRAM(dict(enumerate(text)))
        data = SimpleRAM()
        processor = BFProcessor(commands, program, data)
        processor.process()
