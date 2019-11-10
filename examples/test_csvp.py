import unittest
from parsec import *
from csvp import *

class TestCSVP(unittest.TestCase):

    def test_cell(self):
        self.assertEqual(cell.parse('cell'), 'cell')

    def test_cells(self):
        self.assertEqual(cells.parse('cell,cell'), ['cell'] * 2)
        self.assertEqual(cells.parse('"large, cell, thing",cell'),
                         ["large, cell, thing", 'cell'])
        self.assertNotEqual(cells.parse('"large, cell, thing", cell'),
                          ["large, cell, thing", 'cell'])

    def test_table(self):
        cells = ['cell'] * 2
        self.assertNotEqual(table.parse('cell,cell \n cell,cell '), [cells] * 2)
        self.assertEqual(table.parse('cell,cell\ncell,cell'), [cells] * 2)

    def test_quoted_cell(self):
        self.assertEqual(cell.parse('"cell"'), 'cell')
        self.assertEqual(cell.parse('"ce""ll"'), 'ce"ll')
        self.assertEqual(cell.parse('"large, cell, thing", cell'), "large, cell, thing")
        self.assertEqual(cell.parse('"ce"ll'), 'ce')
        self.assertEqual(cell.parse('c"e"ll'), 'c"e"ll')
        
if __name__ == '__main__':
    unittest.main()
