from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']

cloud_config= {
        'secure_connect_bundle': 'secure-connect-letsshill.zip'
}
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select * from ls.accounts").one()
if row:
    print(row)
else:
    print("An error occurred.")
