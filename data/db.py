from pony.orm import Database

db = Database()
db.bind(provider='mysql', host='localhost', port=3306, user='root', password='Ferraro22', db='caseBackend')