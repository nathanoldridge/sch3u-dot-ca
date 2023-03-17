from flask import Flask, render_template

# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>Chemistry Practice</title>
    <link rel="stylesheet" href="static/style.css" />
    </head>\n<body>
    <a href="/">Home</a> <a href="/about">About</a><hr />'''
homepagetext = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
#home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'
about_text = '''<h1>SCH3U</h1><hr /><p>This app was written by Nathan
    Oldridge (ChemistNate).'''

# EB looks for an 'application' callable by default.
application = Flask(__name__)

# add a rule for the index page.
application.add_url_rule('/', 'index', (lambda: header_text +
    say_hello() + homepagetext + footer_text))

application.add_url_rule('/about', 'about', (lambda: header_text +
    about_text + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
#application.add_url_rule('/<username>', 'hello', (lambda username:
#    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()