from zebra import zebra
import Constants


class Printer(object):

    def __init__(self):
        self.z_printer = zebra.zebra(Constants.PRINTER_NAME)
        self.z_printer.setup(
            direct_thermal=False,
            label_height=(600, 12),
            label_width=800
        )

    def print_ticket(self, num):
        self.z_printer.output(Constants.TICKET_TEMPLATE % 'Ticket ' + num)
