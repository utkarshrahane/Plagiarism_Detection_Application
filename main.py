from flask import Flask, render_template, request, url_for
import similarity

#Creating app instance for the Flask server.

app = Flask(__name__, template_folder='Templates')

#Creating routes for the web pages to be redirected.

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')


@app.route('/report',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['text']

      if len(result) == 0:
         resultf = request.files['myfile']
         
         result = {'myfile': resultf.read()}
      test=  similarity.returnTable(similarity.report(str(result)))
      
      return render_template('report.html', PWM_value=test)
   

#Below is the driver code for running flask server for the application.
#The localhost and port is defined for the server to run the application on.

if __name__ == '__main__':
   app.run(debug = True, host='127.0.0.1', port=5555)
