from flask import Flask, render_template, request

app = Flask(__name__)

authorized_ip = []

@app.route('/')
def home():
    ip = request.remote_addr
    if ip in authorized_ip:
        return render_template('authorized.html')
    
    return render_template('index.html')

@app.route('/authorized')
def authorized():
    ip = request.remote_addr
    if ip in authorized_ip:
        return render_template('authorized.html')
    
    return render_template('index.html')

'''@app.route('/robots.txt')
def robots():
    
    return open('robots.txt').read()'''

@app.route('/todo')
def secret():
    
    return render_template('secret_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print('adjhadkabd;aodb;ob')
    print(request.data)
    
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        js = request.get_json()
        print(js['username'])
        username = js['username']
        password = js['password']
        if username == 'Apelsin' and password == 'blabla':
            authorized_ip.append(request.remote_addr)
            return "Welcome"
        else:
            return 'no'
    else:
        return 'govno'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 80)
