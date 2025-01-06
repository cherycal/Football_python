import datetime

from modules import sqldb

fdb = sqldb.DB('Football.db')

fdb.table_to_html("PlayerDashboard")

print(datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))
