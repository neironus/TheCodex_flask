from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "hello world!"

@app.route('/blog')
def blog():
    return 'This is the blog'

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return f'This is blog post {blog_id}'

# or
# @app.route('/blog/<blog_id>')
# def blogpost(blog_id):
#     return f'This is blog post {str(blog_id)}'

if __name__ == '__main__':
    app.run()
