import login as login
from flask import Flask
from flask import request
from flask_jwt_extended import create_access_token

app = Flask(__name__)


@login.route('/login', methods=['POST'])
def signin():
    data = request.get_json()

    login = data['login']
    password = data['password']

    con = sqlite3.connect("etl.db")
    cur = con.cursor()

    query = "SELECT user_id FROM users WHERE (login=? OR email=?) AND password=?"
    user_raw = cur.execute(query, (login, login, password))
    user_id = user_raw.fetchone()[0]

    # TO-DO: If user_id is not okay
    if user_id is not None:
        access_token = create_access_token(identity=user_id)
        response = {"access_token": access_token, 'user_id': user_id}
    else:
        # TO-DO: handle login
        return {"message": "Wrong email or password"}, 401
    return response


if __name__ == "__main__":
    app.run(debug=True)
