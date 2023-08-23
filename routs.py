from flask import Flask
from views import AdView

app = Flask("app") # what is a flask?
# Answer: Flask is a micro web framework written in Python for creating websites and applications.

app.add_url_rule("/advertisements/<int:id_ad>/", view_func=AdView.as_view('advertisements_delete'),
                 methods=['DELETE', 'GET'])
app.add_url_rule("/advertisements", view_func=AdView.as_view('advertisements_create'), methods=['POST'])
