from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db, app
from project.server.models import User

users_blueprint = Blueprint('users', __name__)


class GetUserList(MethodView):
    def get(self):
        ret = []
        userList = User.query.all()
        for user in userList:
            ret.append({'ID': user.id, 'Email': user.email})
        return make_response(jsonify(ret)), 201


user_list_view = GetUserList.as_view('user_api')

users_blueprint.add_url_rule(
    '/users/index',
    view_func=user_list_view,
    methods=['GET']
)
