from flask import Flask
from routes import Router
import Constants

def main():
    print('Starting Server')
    app = Flask(__name__)
    router = Router.Router(app)
    router.manage_routes()
    app.run(host=Constants.HOST, port=Constants.PORT)


if __name__ == '__main__':
    main()
