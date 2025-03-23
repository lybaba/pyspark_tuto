from datetime import datetime, date
from pyspark.sql import Row
import pyspark.sql.functions as f
from pyspark.sql.functions import from_csv, col
from pprint import pprint

df = spark.createDataFrame([
    Row(identifiant_si='a1', items=['1,poste_source,5,depart_htb', '6,cable_interne,8,troncon']),
    Row(identifiant_si='a1', items=['2,poste_source,6,depart_htb', '2,cable_interne,9,troncon']),
])

df = df.select(
    'identifiant_si',
    f.explode(f.col('items')).alias('item')
)


col_schema = ["node1_id STRING", "node1_type STRING", "node2_id STRING", "node2_type STRING"]
schema_str = ",".join(col_schema)
options = {'sep': ","}

df = df.select(
    df.identifiant_si,
    from_csv(df.item, schema_str, options).alias("nodes")
)

nbPostes = df.filter(df.nodes.node1_type == 'poste_source').count()
print( "nbPostes: {}".format(nbPostes))

for row in df.collect():
    #pprint(row.nodes.node1)
    print('{} {} {} {} {}'.format(row.identifiant_si, row.nodes.node1_id,row.nodes.node1_type, row.nodes.node2_id,  row.nodes.node2_type))


df = df.select(
        df.identifiant_si,
        df.nodes.node1_id.alias("node1_id"),
        df.nodes.node1_type.alias("node1_type"),
        df.nodes.node2_id.alias("node2_id"),
        df.nodes.node2_type.alias("node2_type")
)
df.printSchema()

df.coalesce(1).write.option("header",True).mode("overwrite").csv("./output.txt")

