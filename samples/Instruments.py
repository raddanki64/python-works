
class Instrument():
    def __init__(self, ticker, price):
        self.ticker = ticker
        self.price = price

    def dump(self):
        print(self.ticker)
        print(self.price)

class FixedIncomeInstrument(Instrument):
    def __init__(self, ticker, price, irate):
        Instrument.__init__(self, ticker, price)
        self.irate = irate

    def dump(self):
        super().dump()
        print(self.irate)

i1 = Instrument("IBM", 75.00)
i1.dump()

f1 = FixedIncomeInstrument("MSFT", 82.00, 3.5)
f1.dump()





