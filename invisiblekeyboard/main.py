import webapp2
import cgi
import jinja2
from parsing_keystrokes import parse_keystrokes
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

MAIN_PAGE_HTML = """\
<html>
  <body>
    <form action="/translate" method="post">
      <div><textarea name="content" rows="3" cols="60"></textarea></div>
      <div><input type="submit" value="Submit for Translation"></div>
    </form>
  </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

class Translate(webapp2.RequestHandler):
    def post(self):
        keystrokes = self.request.get('content')
#        self.response.write(keystrokes)
        translation = self.translate(keystrokes)
        self.response.write(translation)

    def translate(self, keystrokes):
        translation = parse_keystrokes(keystrokes)
        template_values = {
            "sentence":translation
        }
        template = JINJA_ENVIRONMENT.get_template("translation.html")
        return template.render(template_values)


application = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/translate', Translate)
], debug=True)
