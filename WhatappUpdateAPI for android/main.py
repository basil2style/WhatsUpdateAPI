from flask import Flask,jsonify
import scraper

app = Flask(__name__)

@app.route('/')
def hello_world():
   link,ver = scraper.main()
   return jsonify(link=link,
                   version=ver)


if __name__ == '__main__':
    app.run()
