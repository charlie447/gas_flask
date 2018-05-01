from start import db,Gas,Users

user = Users.query.filter_by(username="admin1").first()

print(user)