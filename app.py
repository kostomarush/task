from flask import Flask, request, render_template_string, render_template, request, redirect, url_for

app = Flask(__name__)

# Простая имитация базы данных для хранения учетных данных
users = {
    'john': {'password': 'secret'},
    'jane': {'password': 'jj211'},
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'jane' and users[username]['password'] == password:
        return render_template('flag.html')

    elif username in users and users[username]['password'] == password:
        # В данном примере успешная авторизация просто перенаправляет на другую страницу
        # В реальном приложении здесь могут быть дополнительные шаги, например, установка сессии
        return redirect(url_for('dashboard'))

    else:
        # В случае ошибки авторизации, можно добавить соответствующее сообщение
        return render_template('login.html', error='Invalid credentials')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():        
    if request.method == 'POST':
        return render_template_string(request.form.get('c'))

    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)
    
