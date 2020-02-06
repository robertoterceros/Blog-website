from flask import Flask, flash
from flask import render_template, redirect
from flask import url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# To protect coockies
app.config['SECRET_KEY'] = 'eb9f68411f660544845fb2043eaf62b5'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 10, 2018'
    },
    {
        'author': 'Roberto Terceros',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 11, 2019'
    }
]

@app.route("/") # Decorator anade information a funciones existentes
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsucessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__=='__main__':
    app.run(debug=True)
