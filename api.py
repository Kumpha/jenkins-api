from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message":"Index"}

@app.route("/getcode")
def hello():
    return {"message":"Test featured"}

@app.route("/plus/<num1>/<num2>")
def plus(num1,num2):
    return {"result":(float(num1)+float(num2))}

@app.route("/is_prime/<num>")
def isPrime(num):
    num = int
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    
    

if __name__ == '__main__':
      app.run(port=5000)
 