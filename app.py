#s-1: import flask from Flask object
from flask import Flask,request,render_template      #flask=module,Flask=class  #request="if we want to request anything from user 
                                     #like /add in our code we shouladd request in step1.
import re


#s2:   create a object with parameter name __name__
app = Flask(__name__)
user_names=['amma','nanna','anna','yash']
##############################################################
#S-3: important step which we write logic for our web app and res other steps are common for alll web app
#Creating a route and binding with functionality
@app.route('/')
def homepage():
    return render_template('reg.html') 
@app.route('/reg',methods=['GET','POST'])
def reg1():
    text_string = request.form['text_string']
    regular_expression = request.form['regular_expression']
    matches=re.findall(regular_expression,text_string)
    count=len(matches)
    return render_template('regresult.html', matches=matches,count=count)   



#s-4: Run the app
if __name__ =='__main__':
    app.run(debug=True)

