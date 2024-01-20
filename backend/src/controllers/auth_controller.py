from flask import request, Response, json, Blueprint

# auth controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)

# route for Register.
@auth.route('/register', methods = ["POST"])
def handle_register():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

# route for Login.
@auth.route('/login', methods = ["POST"])
def handle_login():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )

# route for Logout.
@auth.route('/logout')
def handle_logout():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )