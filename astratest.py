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

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")