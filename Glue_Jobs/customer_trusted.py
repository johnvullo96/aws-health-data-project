import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1709016332232 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://jv-stedi-project/customer/landing/"], "recurse": True}, transformation_ctx="AmazonS3_node1709016332232")

# Script generated for node Privacy Filter
PrivacyFilter_node1709016565342 = Filter.apply(frame=AmazonS3_node1709016332232, f=lambda row: (not(row["shareWithResearchAsOfDate"] == 0)), transformation_ctx="PrivacyFilter_node1709016565342")

# Script generated for node Target Customer Zone
TargetCustomerZone_node1709016643769 = glueContext.getSink(path="s3://jv-stedi-project/customer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="TargetCustomerZone_node1709016643769")
TargetCustomerZone_node1709016643769.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="customer_trusted")
TargetCustomerZone_node1709016643769.setFormat("glueparquet", compression="snappy")
TargetCustomerZone_node1709016643769.writeFrame(PrivacyFilter_node1709016565342)
job.commit()
