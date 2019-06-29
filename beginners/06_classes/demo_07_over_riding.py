# Parent class
class Printer:
    def print(self):
        print('Generic Printer')


# Child Class
class DotMatrixPrinter(Printer):
    # override method in parent
    def print(self):
        print('A Dot matrix printer')


# Child Class
class InkJetPrinter(Printer):
    # override method in parent
    def print(self):
        print('Ink jet print')


# Utility function
def send(printer):
    printer.print()


if __name__ == '__main__':
    dotMatrixPrinter = DotMatrixPrinter()
    inkJetPrinter = InkJetPrinter()
    send(dotMatrixPrinter)
    send(inkJetPrinter)
