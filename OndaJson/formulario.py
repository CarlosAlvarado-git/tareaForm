from flask import Flask, url_for, request, redirect
from jinja2 import Template, Environment, FileSystemLoader
import json
import os
File_loader = FileSystemLoader("templates")
env = Environment(loader=File_loader)
app = Flask(__name__)
print(os.getcwd())
with open("OndaJson\\form.json") as json_file:
    myjson = json.load(json_file)
@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        _id = request.form['id']
        _name = request.form['name']
        _age = request.form['age']
        _uni = request.form['uni']

        myjson['data'].append({"id":_id, "name":_name,"age":_age,"uni":_uni})
        return redirect('index.html')
    template = env.get_template('form.html')
    return template.render()

@app.route('/')
def index():
    template = env.get_template('index.html')
    return template.render(my_json=myjson['data'], headers=myjson['headers'])

if __name__ == '__main__':
    app.run()
