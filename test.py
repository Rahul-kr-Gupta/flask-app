from hashids import Hashids

from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'
hashids = Hashids(min_length=4, salt= app.config['SECRET_KEY'])

hashid = hashids.encode(12)
print('hashid',hashid)
# hashid qlr1

decode = hashids.decode('2GW2')
print('decode',decode)
# decode (1,)