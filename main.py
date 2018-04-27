from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(4000))

    def __init__(self, title, body):  
        self.title = title
        self.body = body

@app.route('/newpost', methods=['POST', 'GET'])
def add_post():
    
    if request.method == 'POST':
        title = request.form['post-title']
        body = request.form['post-body']
        new_post = Blog(title, body)
        
        db.session.add(new_post)
        db.session.commit()
        
        return redirect('/blog')
        
    else:

        return render_template('newpost.html')

@app.route('/blog', methods=['POST','GET'])
def my_blog():

    blog = Blog.query.filter_by().all()

    return render_template('blog.html', blog=blog)
        
@app.route('/', methods=['POST', 'GET'])
def index():
    
    return render_template('base.html', my_blog=my_blog)

if __name__ == '__main__':
    app.run()