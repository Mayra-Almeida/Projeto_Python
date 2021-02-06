from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operacao']

        if (num1 != '' and num2 != ''):

            if operation == 'soma':
                sum = int(num1) + int(num2)
                return render_template('index.html', sum=sum)

            elif operation == 'subt':
                sum = int(num1) - int(num2)
                return render_template('index.html', sum=sum)

            elif operation == 'mult':
                sum = int(num1) * int(num2)
                return render_template('index.html', sum=sum)

            elif operation == 'mod':
                sum = int(num1) % int(num2)
                return render_template('index.html', sum=sum)

            elif operation == 'pot':
                sum = int(num1) ** int(num2)
                return render_template('index.html', sum=sum)

            elif operation == 'divi':
                if (num2 != '0'):
                    sum = int(num1) / int(num2)
                    return render_template('index.html', sum=sum)
                else:
                    return render_template('index.html', sum='Não é possível dividir por zero')

        else:
            return render_template('index.html', sum='Preencha os dois números')


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html')


app.run(port = 8080, debug = True)