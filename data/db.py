from pony.orm import Database

db = Database()
db.bind(provider='sqlserver', host='localhost', port=3306, user='admin', password='admin', db='caseBackend')