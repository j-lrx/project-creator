from flask import Flask, request
from datetime import datetime, timedelta
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        
        full_name = f"{first_name.lower().replace(' ', '-')}_{last_name.lower().replace(' ', '-')}"

        budget = 15
        end_date = (datetime.now() + timedelta(days=90)).strftime('%Y-%m-%d')

        doc_ref = db.collection(u'projects').document(full_name)
        doc_ref.set({
            u'full_name': full_name,
            u'first_name': first_name,
            u'last_name': last_name,
            u'email': email,
            u'budget': budget,
            u'end_date': end_date
        })
        
        return f"Project {full_name} created successfully with email {email}."
    
    return '''
        <form method="post">
            <label for="first_name">First Name:</label>
            <input type="text" id="first_name" name="first_name"><br><br>

            <label for="last_name">Last Name:</label>
            <input type="text" id="last_name" name="last_name"><br><br>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>

            <input type="submit" value="Create Project">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
