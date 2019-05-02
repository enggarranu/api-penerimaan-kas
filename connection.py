import MySQLdb

def get_db():
    # Open database connection
    db = MySQLdb.connect("localhost","root","Password@1","db_penerimaan_kas" )
    # db = MySQLdb.connect("47.74.245.145","root","Password@1","db_koperasi" )
    return db

