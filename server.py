from flask import Flask, render_template, request, redirect
import csv 
app = Flask(__name__)


@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		database.write('\n{0},{1},{2}'.format(data['email'],data['subject'],data['message']))
		
def write_to_csv(data):
	with open('database.csv', newline='', mode='a') as database2:
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([data['email'],data['subject'],data['message']])
			

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
	   data = request.form.to_dict()
	   write_to_file(data)
	   write_to_csv(data)
	   return redirect('/thankyou.html')
	else:
		return 'Something went wrong!'








