import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1712476359321 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="accelerometer_landing", transformation_ctx="AccelerometerLanding_node1712476359321")

# Script generated for node Customer Trusted
CustomerTrusted_node1712476375441 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_trusted", transformation_ctx="CustomerTrusted_node1712476375441")

# Script generated for node Rename User Field
RenameUserField_node1712476389949 = RenameField.apply(frame=AccelerometerLanding_node1712476359321, old_name="user", new_name="user_acc", transformation_ctx="RenameUserField_node1712476389949")

# Script generated for node Rename Timestamp Field
RenameTimestampField_node1712476405262 = RenameField.apply(frame=RenameUserField_node1712476389949, old_name="timestamp", new_name="timestamp_acc", transformation_ctx="RenameTimestampField_node1712476405262")

# Script generated for node SQL Query
SqlQuery0 = '''
select
    acc.user_acc
    ,acc.timestamp_acc
    ,acc.x
    ,acc.y
    ,acc.z
FROM acc
INNER JOIN ct ON ct.email = acc.user_acc
'''
SQLQuery_node1712476415539 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"acc":RenameTimestampField_node1712476405262, "ct":CustomerTrusted_node1712476375441}, transformation_ctx = "SQLQuery_node1712476415539")

# Script generated for node Amazon S3
AmazonS3_node1712476515879 = glueContext.getSink(path="s3://jv-stedi-project/accelerometer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1712476515879")
AmazonS3_node1712476515879.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="accelerometer_trusted")
AmazonS3_node1712476515879.setFormat("glueparquet", compression="snappy")
AmazonS3_node1712476515879.writeFrame(SQLQuery_node1712476415539)
job.commit()

