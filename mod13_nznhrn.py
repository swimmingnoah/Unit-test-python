import unittest
import main


class test_stock_visualiser(unittest.TestCase):

    def test_symbol(self):
        self.assertEqual(main.isTickerSymbolUpper("AMD"), ("AMD"))
        self.assertEqual(main.isTickerSymbolUpper("amd"), ("AMD"))
        self.assertEqual(main.isTickerSymbolLengthValid("N"), True)
        self.assertEqual(main.isTickerSymbolLengthValid("NNNNNN"), True)
        self.assertEqual(main.isTickerSymbolLengthValid("NNNNNNNN"), False)
        self.assertEqual(main.isTickerSymbolLengthValid(""), False)
        self.assertEqual(main.isTickerSymbolAlpha("AAA"), True)
        self.assertEqual(main.isTickerSymbolAlpha("AMD"), True)
        self.assertEqual(main.isTickerSymbolAlpha("123"), False)
        self.assertEqual(main.isTickerSymbolAlpha("12A"), False)

    def test_chart(self):
        self.assertEqual(main.isChartValid(1), False)
        self.assertEqual(main.isChartValid(2), False)
        self.assertEqual(main.isChartValid(3), True)
        self.assertEqual(main.isChartValid(-1), True)

    def test_time(self):
        self.assertEqual(main.isTimeSeriesValid(1), False)
        self.assertEqual(main.isTimeSeriesValid(2), False)
        self.assertEqual(main.isTimeSeriesValid(3), False)
        self.assertEqual(main.isTimeSeriesValid(4), False)
        self.assertEqual(main.isTimeSeriesValid(6), True)
        self.assertEqual(main.isTimeSeriesValid(-1), True)

    def test_start_date(self):
        self.assertEqual(main.validate("1999-07-10"), True)
        self.assertEqual(main.validate("2021-04-22"), True)
        self.assertEqual(main.validate("21-04-25"), False)

    def test_end_date(self):
        self.assertEqual(main.validate("1999-07-10"), True)
        self.assertEqual(main.validate("2021-04-22"), True)
        self.assertEqual(main.validate("21-04-25"), False)


if __name__ == "__main__":
    unittest.main()
