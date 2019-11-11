from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Ben Myles',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '2019-10-18'
    },
    {
        'author': 'Ben Tyler',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '2019-10-19'
    }
]

@app.route('/')
@app.route('/home')
def root():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
