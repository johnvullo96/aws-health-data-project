import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1711226442309 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_trusted", transformation_ctx="AWSGlueDataCatalog_node1711226442309")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1711226459639 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="accelerometer_trusted", transformation_ctx="AWSGlueDataCatalog_node1711226459639")

# Script generated for node Join
Join_node1711226475965 = Join.apply(frame1=AWSGlueDataCatalog_node1711226459639, frame2=AWSGlueDataCatalog_node1711226442309, keys1=["user"], keys2=["email"], transformation_ctx="Join_node1711226475965")

# Script generated for node Drop Fields
DropFields_node1711226502541 = DropFields.apply(frame=Join_node1711226475965, paths=["z", "y", "user", "x", "timestamp"], transformation_ctx="DropFields_node1711226502541")

# Script generated for node Drop Duplicates
DropDuplicates_node1711226513447 =  DynamicFrame.fromDF(DropFields_node1711226502541.toDF().dropDuplicates(), glueContext, "DropDuplicates_node1711226513447")

# Script generated for node Amazon S3
AmazonS3_node1711226543408 = glueContext.getSink(path="s3://jv-stedi-project/customer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1711226543408")
AmazonS3_node1711226543408.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="customer_curated")
AmazonS3_node1711226543408.setFormat("glueparquet", compression="snappy")
AmazonS3_node1711226543408.writeFrame(DropDuplicates_node1711226513447)
job.commit()
