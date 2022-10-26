import unittest
from funcs import *

class TestCases(unittest.TestCase):
    def test_check_forward01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((9,3), check_forward(puzzle0, "UNIX"))

    def test_check_forward02(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((7,2), check_forward(puzzle0, "SLO"))

    def test_check_forward03(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((1,0), check_forward(puzzle1, "ZEBRA"))

    def test_check_forward04(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((2,2), check_forward(puzzle1, "RACCOON"))

    def test_check_forward05(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((5,3), check_forward(puzzle2, "CHORRO"))

    def test_check_forward06(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((1,6), check_forward(puzzle2, "MILL"))

    def test_check_backward01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((1,4), check_backward(puzzle0, "VIM"))

    def test_check_backward02(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((1,6), check_backward(puzzle1, "BEAR"))

    def test_check_backward03(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((2,9), check_backward(puzzle2, "HIGH"))

    def test_check_backward04(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((2,9), check_backward(puzzle2, "HIGHLAND"))

    def test_check_down01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((1,0), check_down(puzzle0, "CALPOLY"))

    def test_check_down02(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((1,3), check_down(puzzle1, "RABBIT"))

    def test_check_down03(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((0,4), check_down(puzzle2, "SLACK"))

    def test_check_down04(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((4,6), check_down(puzzle2, "GRAND"))

    def test_check_down05(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((5,5), check_down(puzzle2, "OSOS"))

    def test_check_down06(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((0,7), check_down(puzzle2, "HIGUERA"))

    def test_check_up01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((6,8), check_up(puzzle0, "COMPILE"))

    def test_check_up02(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((8,8), check_up(puzzle1, "CHICKEN"))

    def test_check_up03(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((6,2), check_up(puzzle2, "BROAD"))

    def test_check_up04(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((6,9), check_up(puzzle2, "MARSH"))

    def test_check_up05(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((7,8), check_up(puzzle2, "FOOTHILL"))

    def test_check_up06(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((9,9), check_up(puzzle2, "PALM"))

    def test_check_diagonal01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual((1,0), check_diagonal(puzzle0, "CPE"))

    def test_check_diagonal02(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual((4,0), check_diagonal(puzzle1, "CORER"))

    def test_check_diagonal03(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((4,4), check_diagonal(puzzle2, "KOAD"))

    def test_check_diagonal04(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual((0,6), check_diagonal(puzzle2, "AIIS"))

    def test_find_word01(self):
        puzzle0 = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual("CALPOLY: (DOWN) row: 1 column: 0", find_word(puzzle0, "CALPOLY"))

    def test_find_word02(self):
        puzzle1 = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual("BEAR: (BACKWARD) row: 1 column: 6", find_word(puzzle1, "BEAR"))

    def test_find_word03(self):
        puzzle2 = "LLARSHAHLCAOOLLAMILLOIDNALHGIHRBAMCETUHSSMOSKAGETRCORCHORROAIDBSLSAAOMIGOSMONDFLHHNGMSDCMACMIRRSMLHP"
        self.assertEqual("PEACH: word not found", find_word(puzzle2, "PEACH"))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()