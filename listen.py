import string
from urllib.parse import quote
from mitmproxy import ctx
import json
import requests

def response(flow):
    global order
    path = flow.request.path
    if path == '/wxa/api/getCircleQuizFeed':
        data = json.loads(flow.response.text)
        try:
            question = data['data']['feeds'][0]['field']['question']['content']
            options = data['data']['feeds'][0]['field']['question']['options']
            ctx.log.info('question : %s, options : %s'%(question, options))
            options = ask(question, options)
            data['data']['feeds'][0]['field']['question']['options'] = options
            flow.response.text = json.dumps(data)
        except:
            pass

def ask(question, options):

    url = quote('http://www.baidu.com/s?wd=' + question, safe=string.printable)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}
    content = requests.get(url, headers=headers).text
    answer = []
    for option in options:
        count = content.count(option)
        ctx.log.info('option : %s, count : %s'%(option, count))
        answer.append(option + ' [' + str(count) + ']')
    return answer