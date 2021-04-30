import ibm_db
conn = ibm_db.connect("DATABASE=BLUDB;HOSTNAME=dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=mtg35399;PWD=f7wr9t558@wd3kt1;", "", "")

def get_Data():
    data = []
    if conn:
        sql = "SELECT * FROM MTG35399.test"
        stmt = ibm_db.exec_immediate(conn, sql)
        result = ibm_db.fetch_both(stmt)
        while(result):
            result = ibm_db.fetch_both(stmt)
            data.append(result)
        return data

datos = get_Data()
