from start import db,Gas,Users

user = Users.query.filter_by(username="admin").first_or_404()

print(user)