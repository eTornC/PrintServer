import json
from printing.Printer import Printer


class Router(object):

    def __init__(self, app):
        self.appFlask = app
        self.printer = Printer()

    def manage_routes(self):

        app = self.appFlask
        printer = self.printer

        @app.route('/print/<turn>/<num>', methods=['POST'])
        def print_ticket(turn,num):

            printer.print_ticket(turn,num)

            return json.dumps({
                'turn':turn,
                'number': num,
                'printed': True
            })

        @app.route('/print/<num>', methods=['GET'])
        def get_print_ticket(num):
            return json.dumps({
                'number': num,
                'printed': 'Fes POST'
            })
