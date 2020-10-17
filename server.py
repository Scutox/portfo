from flask import Flask, render_template, url_for, request, redirect
import os
import csv
app = Flask(__name__)
app._static_folder = ''
print(__name__)

#print(os.getcwd())
#os.chdir('/home/paul/Desktop/Python/web server')


@app.route('/<page_name>')
def html_page(page_name):
     return render_template(page_name)


def write_to_file(data):
     with open('database.txt', mode='a') as database:
          email = data["email"]
          subject = data["subject"]
          message = data["message"] 
          file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
     with open('database1.csv', mode='a') as database2:
          email = data["email"]
          subject = data["subject"]
          message = data["message"] 
          csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
          csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
     if request.method == 'POST':
          try:
               data = request.form.to_dict()
               print(data)
               write_to_csv(data)
               return redirect('thankyou.html')
          except:
               return 'did not save to database'
     else:
          return 'Something went wrong'






# @app.route('/')
# def my_home():
#      return render_template('./index.html')

# @app.route('/index.html')
# def index():
#      return render_template('./index.html')

# @app.route('/works.html')
# def blog():
#      return render_template('./works.html')

# @app.route('/contact.html')
# def contact():
#      return render_template('./contact.html')

# @app.route('/about.html')
# def about():
#      return render_template('about.html')

# @app.route('/components.html')
# def components():
#      return render_template('components.html')     

# @app.route('/blog/<username>/<int:postID>')
# def blog_name(username, postID):
#      return render_template('index.html', username = username, postID = postID) 