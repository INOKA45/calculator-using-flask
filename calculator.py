from flask import Flask,render_template,request

app =  Flask(__name__)

@app.route("/")
def home():
    return render_template("calculator.html")
    

@app.route("/add",methods=["POST"])    
def add():
    num1 = request.form.get("number1")
    num2 = request.form.get("number2")
    operation1 = request.form.get("ADD")
    operation2 = request.form.get("SUB")
    operation3 = request.form.get("MUL")
    operation4 = request.form.get("DIV")
    a=int(num1)
    b=int(num2)
    if operation1:
        operation_name="Addition"
        answer = a + b
    elif operation2:
        operation_name="Subtraction"
        answer = a-b
    elif operation3:
        operation_name="Multiplication"
        answer = a * b
    elif operation4:
        operation_name="Division"
        answer = a/b
    
    return render_template("answer.html",ans=answer,operation=operation_name)