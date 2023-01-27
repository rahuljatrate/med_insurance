from flask import Flask , jsonify, request, render_template,json
import pickle
import numpy as np
app = Flask(__name__)
# print(__name__)  # __main__

# model = pickle.load(open("project_app\Linear_Model.pkl",'rb'))

class LinearModel:
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region

    def get_pickel(self):
        self.p = pickle.load(open('project_app\Linear_Model.pkl', 'rb'))
 

    def get_details(self):

        columns_names = np.array(['age', 'sex', 'bmi', 'children', 'smoker', 'region_northeast',
     'region_northwest', 'region_southeast', 'region_southwest'],ndmin=2)

        region_index = np.where(columns_names == self.region)[1]
        test_array = np.zeros(columns_names.shape[1])

        test_array[0] = self.age
        test_array[1] = self.sex
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.smoker
        test_array[region_index] = 1

        result = np.around(self.p.predict([test_array]), 2)
        return result[0]


@app.route('/',methods=["GET","POST"]) 
def hello_flask():
    print('Welcome to Flask Session')
    if request.method== "POST":
        sex = request.form.get('gender')
        smoker = request.form.get('smoker')
        age = request.form.get('age')
        children = request.form.get('Children')
        # children=2
        BMI =request.form.get('BMI')
        region = request.form.get('region')
        # print(sex)
        obj = LinearModel(age,sex,BMI,children,smoker,region)
        obj.get_pickel()
 
            
        return render_template("home.html",output = obj.get_details())

    else:
        result = ""
        return render_template("home.html",output = result)

app.run()