from start import db

class Gas(db.Model):
    __tablename__ = 'gas_repair_info'
    _mobile = db.Column(db.String(100))
    _account = db.Column(db.String(100))
    _date = db.Column(db.String(20))
    _area = db.Column(db.String(20))
    _type = db.Column(db.Integer)
    _address = db.Column(db.String(100))
    _order_id = db.Column(db.String(100),primary_key=True) 

    def __init__(self,_mobile,_account,_date,_area,_type,_address,_order_id):
        self._mobile = _mobile
        self._account = _account
        self._date = _date
        self._area = _area
        self._date = _date
        self._type = _type
        self._address = _address
        self._order_id = _order_id

    def __repr__(self):
        return '<Mobile: %r>' % self._mobile