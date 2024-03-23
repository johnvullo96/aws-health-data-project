import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1711226789117 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_curated", transformation_ctx="AWSGlueDataCatalog_node1711226789117")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1711226774536 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="step_trainer_landing", transformation_ctx="AWSGlueDataCatalog_node1711226774536")

# Script generated for node Join
Join_node1711226808495 = Join.apply(frame1=AWSGlueDataCatalog_node1711226774536, frame2=AWSGlueDataCatalog_node1711226789117, keys1=["serialnumber"], keys2=["serialnumber"], transformation_ctx="Join_node1711226808495")

# Script generated for node Drop Fields
DropFields_node1711226837269 = DropFields.apply(frame=Join_node1711226808495, paths=["`.serialnumber`", "birthday", "sharewithpublicasofdate", "sharewithresearchasofdate", "registrationdate", "customername", "sharewithfriendsasofdate", "email", "lastupdatedate", "phone"], transformation_ctx="DropFields_node1711226837269")

# Script generated for node Amazon S3
AmazonS3_node1711226863218 = glueContext.getSink(path="s3://jv-stedi-project/step-trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1711226863218")
AmazonS3_node1711226863218.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="step_trainer_trusted")
AmazonS3_node1711226863218.setFormat("glueparquet", compression="snappy")
AmazonS3_node1711226863218.writeFrame(DropFields_node1711226837269)
job.commit()
