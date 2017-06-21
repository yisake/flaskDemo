from admin_views import *
from flask import Flask,render_template

app=Flask('my_application')

@app.route('/')
def app_index():
    return render_template('index.html')

if __name__=='__main__' :
    app.register_blueprint(admin,url_prefix='/admin')
    app.run(host='0.0.0.0', port=5000, debug=True)