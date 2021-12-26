from flask import Flask, request, jsonify
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(r'C:\Users\hidet\PycharmProjects\grable_api\chromedriver.exe', options=options)
driver.get('https://gbs.eriri.net/')
driver.execute_script("document.querySelector('#center > div:nth-child(1) > div.head > a').click()")
driver.execute_script(
    "document.querySelector('#center > div:nth-child(1) > div.modal-wrap > div > div > div > section:nth-child(2) > div > ul.tag-list > li:nth-child(2) > label').click()")
driver.execute_script(
    "document.querySelector('#center > div:nth-child(1) > div.modal-wrap > div > div > div > section:nth-child(2) > div > ul.enemy-list > li:nth-child(4) > a > span.data').click()")
driver.execute_script(
    "document.querySelector('#center > div:nth-child(1) > div.modal-wrap > div > footer > a.right.btn-1').click()")
sleep(2)


@app.route('/', methods=["GET"])
def api():
    while True:
        sleep(3)
        war = driver.execute_script(
            "return document.querySelector('#center > div:nth-child(1) > div.body > ul > li > a >p.id').textContent;")
        if war is not None:
            break
        else:
            pass
    return jsonify({'war_code': war})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888, debug=True)
