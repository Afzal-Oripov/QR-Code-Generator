from flask import Flask, render_template, request
import segno

app = Flask(__name__) 

@app.route('/', methods=["POST", "GET"])
def home():
    data = request.form.get('value')
    # Проверяем, что данные не пустые
    if data:
        adress = segno.make(data)
    else:
        adress = None
    if request.method == 'POST':
        print(request.form)
    return render_template("index.html", title="Obratnaya svyaz", qrcode=adress)

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "Hello " + name + ': ' + str(id)

if __name__ == "__main__":
    app.run(debug=True)

