from flask import Flask, render_template, request
from flask import flash
from flask import redirect
from flask_wtf import Form
from classes.login_form import LoginForm

app = Flask(__name__)
app.secret_key = "super secret key"
app.debug = True

@app.route("/", methods=['get', 'post'])
def login_view():
	form = LoginForm(request.form or request.args)

	if request.method == 'POST':
		if form.validate():
			flash(request, 'Username and password are correct')
			return redirect('/')

	return render_template('form.html', form=form)

if __name__ == "__main__":
    app.run()