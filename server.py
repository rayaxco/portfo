from flask import Flask,render_template,url_for,request
import os
import datetime,pytz,csv
app=Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/index.html')
def home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def worksclick(page_name):
	return render_template(page_name)

def write_to_file(data):
	filename='messages.txt'
	if os.path.exists(filename):
		email='Email : '+data['email']
		date=str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))+' IndianStandardTime'
		subj='Subject : '+data['subject']
		msg='Message : '+data['message']

		with open('./messages.txt','a') as file:
			file.write(email+'\n')
			file.write(date+'\n')
			file.write('\t'+subj+'\n')
			file.write('\t\t'+msg+'\n\n\n')
	else:
		email='Email : '+data['email']
		date=str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))+' IndianStandardTime'
		subj='Subject : '+data['subject']
		msg='Message : '+data['message']
		with open('./messages.txt','a') as file:
			file.write(email+'\n')
			file.write(date+'\n')
			file.write('\t'+subj+'\n')
			file.write('\t\t'+msg+'\n\n\n')
def write_to_csv(data):
	filename='database.csv'
	if os.path.exists(filename):
		email='Email : '+data['email']
		date=str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))+' IndianStandardTime'
		subj='Subject : '+data['subject']
		msg='Message : '+data['message']
		with open(filename,'a',newline='\n') as file:
			file.write('\n')
			csv_writer=csv.writer(file,delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,date,subj,msg])
	else:
		print('No such file: ',filename)


 	
@app.route('/submit_form', methods=['POST', 'GET'])
def login():
	dict=request.form.to_dict()
	write_to_file(dict)
	write_to_csv(dict)
	return render_template('thankyou.html')
