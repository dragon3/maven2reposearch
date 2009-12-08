import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Search(webapp.RequestHandler):
    def get(self):
        keyword = self.request.get('keyword')
        format = self.request.get('format')
        if format != 'xml' and format != 'html':
            format = 'html'
        artifacts = []
        if keyword:
            for i in ['1','2','3','4']:
                file = open('central-index.' + i + '.txt', 'r')
                while 1:
                    lines = file.readlines(100000)
                    if not lines:
                        break
                    for line in lines:
                        if (line.find(keyword) > -1):
                            splitted = line.split(":")
                            artifacts.append({'group_id': splitted[0], "artifact_id": splitted[1], "version": splitted[2]})
                file.close()
                        
        template_values = {
            'keyword': keyword,
            'artifacts': artifacts,
            }
        path = os.path.join(os.path.dirname(__file__), 'index.' + format)
        if format == 'xml':
            self.response.headers['Content-Type'] = 'text/xml'
        self.response.out.write(template.render(path, template_values))
        
def main():
    application = webapp.WSGIApplication(
        [('/', Search),
         ('/search', Search)],
         debug=True
        )
    wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
    main()
