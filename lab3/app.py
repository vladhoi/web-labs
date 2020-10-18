from flask import Flask, render_template
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'key'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'key'
app.config['TESTING'] = True


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        return '<h1>The username is {}. The password is {}.'.format(
            form.username.data, form.password.data
        )
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
