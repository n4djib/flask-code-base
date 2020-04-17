from flask import Flask, render_template, redirect, request, flash
import time

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/sweet', methods=['POST'])
def sweet():
	data = request.get_json(force=True)


	flash('data: ' + str(data['promo_id']) + ' - ' + str(data['semester_id']))

	# time.sleep(2)

	print(' ')
	print ('Called')
	print (data['promo_id'])
	print(' ')
	# return 'sweet'
	return {"ip": '192.168.1.1'}


# if __name__ == "__main__":
# 	app.run(debug=True, port=5002)