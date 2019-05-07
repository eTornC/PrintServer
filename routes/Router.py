import json
from printing.Printer import Printer


class Router(object):

    def __init__(self, app):
        self.appFlask = app
        self.printer = Printer()

    def manage_routes(self):

        app = self.appFlask
        printer = self.printer

        @app.route('/print/<num>', methods=['POST'])
        def print_ticket(num):

            printer.print_ticket(num)

            return json.dumps({
                'number': num,
                'printed': True
            })

        @app.route('/print/<num>', methods=['GET'])
        def get_print_ticket(num):
            return json.dumps({
                'number': num,
                'printed': 'Fes POST'
            })
