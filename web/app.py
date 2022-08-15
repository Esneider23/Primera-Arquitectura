from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


def search_element(arr, element):
    for i in range(0, len(arr)):
        if element == arr[i]:
            return True
    return False


@app.route('/person_update/<id_person>', methods=['GET'])
def update(id_person):
    data = [i.id_person for i in model]
    aux = [(i.id_person, i.name, i.last_name) for i in model]
    if search_element(data, id_person):
        for z in range(0, len(model)):
            if data[z] == id_person:
                return render_template('update.html', value=aux[z])
    else:
        return render_template('404.html')


@app.route('/person_update/<id_person>', methods=['POST'])
def update_p(id_person):
    name = request.form['Name']
    last_name = request.form['Last_name']
    data = [i.id_person for i in model]
    for z in range(0, len(model)):
        if data[z] == id_person:
            p = Person(id_person=id_person, name=name, last_name=last_name)
            model[z] = p
            return render_template('person_detail.html', value=p)


@app.route('/person_delete/<id_person>', methods=["POST"])
def delete(id_person):
    for z in model:
        if z.id_person == id_person:
            model.remove(z)
            print("word")

    return redirect('/people')


if __name__ == '__main__':
    app.run()