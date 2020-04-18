from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'calendar.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)



class Events(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(250))
	start_event = db.Column(db.DateTime)
	end_event = db.Column(db.DateTime)

	def __repr__(self):
		return '<event: '+self.name+'>'



@app.route('/')
def calendar():
	return render_template('calendar.html')




def generate_modal(event_id):
	event = Events.query.get(event_id)

	return '<h1>Modal for Event id: '+str(event.id)+'</h1>'


@app.route('/load')
def load():
	events = Events.query.all()
	# return str( len(events) )
	# return str( events[0].id )


	data = []
	for event in events:
		# return str(  event['id']  )
		data += [{
			'id': event.id,
			'title': event.name,
			'start': event.start_event.strftime('%Y-%m-%d %H:%M:%S'),
			'end': event.end_event.strftime('%Y-%m-%d %H:%M:%S'),
			'color': 'lightgreen',
			'type': '1',
			'modalContent': generate_modal(event.id)
		}]
	
	return jsonify(data)

@app.route('/insert', methods=['POST'])
def insert():
	# data = request.json
	data = request.get_json(force=True) 

	# print('-------1--------')
	# print('-------2--------')
	# print( str(data['start']) )
	# print( type(data['start']) )
	# print( type( datetime.strptime(data['start'], "%Y-%m-%d %H:%M:%S")  ) )
	# print('-------3--------')
	# print('-------4--------')

	event = Events(
		name=data['title'],
		start_event=datetime.strptime(data['start'], "%Y-%m-%d %H:%M:%S"),
		end_event=datetime.strptime(data['end'], "%Y-%m-%d %H:%M:%S"),
	)
	# title, start:start, end:end
	db.session.add(event)
	db.session.commit()

	return 'event inserted'


@app.route('/update', methods=['POST'])
def update():
	data = request.get_json(force=True) 

	# print('-------1--------')
	# print('-------2--------')
	# print( str(data['id']) )
	# print('-------3--------')
	# print('-------4--------')

	event = Events.query.get( data['id'] )
	# print(str(event.id))
	# print('-------5--------')
	# print('-------6--------')
	
	event.name = data['title']
	event.start_event = datetime.strptime(data['start'], "%Y-%m-%d %H:%M:%S")
	event.end_event = datetime.strptime(data['end'], "%Y-%m-%d %H:%M:%S")
	db.session.commit()

	return 'updated'


@app.route('/delete', methods=['POST'])
def delete():
	data = request.get_json(force=True) 

	# print('-------1--------')
	# print('-------2--------')
	# print( str(data['id']) )
	# print('-------3--------')
	# print('-------4--------')

	event = Events.query.get( data['id'] )
	db.session.delete(event)
	db.session.commit()

	
	return 'removed'