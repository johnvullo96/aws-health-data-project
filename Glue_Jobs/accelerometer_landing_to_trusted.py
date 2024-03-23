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

# Script generated for node Accelerometer Landing Data
AccelerometerLandingData_node1710124650459 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="accelerometer_landing", transformation_ctx="AccelerometerLandingData_node1710124650459")

# Script generated for node Customer Trusted Data
CustomerTrustedData_node1710124656746 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_trusted", transformation_ctx="CustomerTrustedData_node1710124656746")

# Script generated for node Join to Trusted Customer Data
JointoTrustedCustomerData_node1710124334713 = Join.apply(frame1=AccelerometerLandingData_node1710124650459, frame2=CustomerTrustedData_node1710124656746, keys1=["user"], keys2=["email"], transformation_ctx="JointoTrustedCustomerData_node1710124334713")

# Script generated for node Drop Fields
DropFields_node1710828170460 = DropFields.apply(frame=JointoTrustedCustomerData_node1710124334713, paths=["serialnumber", "sharewithpublicasofdate", "birthday", "registrationdate", "sharewithresearchasofdate", "customername", "sharewithfriendsasofdate", "email", "lastupdatedate", "phone"], transformation_ctx="DropFields_node1710828170460")

# Script generated for node Amazon S3
AmazonS3_node1710829583519 = glueContext.getSink(path="s3://jv-stedi-project/accelerometer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1710829583519")
AmazonS3_node1710829583519.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="accelerometer_trusted")
AmazonS3_node1710829583519.setFormat("glueparquet", compression="snappy")
AmazonS3_node1710829583519.writeFrame(DropFields_node1710828170460)
job.commit()
