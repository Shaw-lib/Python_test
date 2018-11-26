import random
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/test')
def test():
    return "Success!"

@app.route('/<born>')
def me(born):
    quotes=['人会长大三次。第一次是在发现自己不是世界中心的时候。第二次是在发现即使再怎么努力，终究还是有些事令人无能为力的时候。第三次是在，明知道有些事可能会无能为力，但还是会尽力争取的时候。',
            '种一棵树最好的时间是十年前，其次是现在。',
            '知道做不到，等于不知道。',
            '无论是谁，都最终在某一刻意识到时间的珍贵，并且几乎注定会因懂事太晚而多少有些后悔。',
            '人生只有900个月。',
            '当初认定是为情所困，过了很久才发现根本是为情欲所困。',
            '每天发生在自己身上的99%的事情对于别人而言根本毫无意义。',
            '不是思考没有用，然而从第三者角度来看，你根本没有改变。',
            '下无根基，上无求索，此为浮躁。']
    quote = random.choice(quotes)
    return render_template('main.html',born=born, quote=quote)

# @app.route('age/<birth>')
# def age(birth):
#     return


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
