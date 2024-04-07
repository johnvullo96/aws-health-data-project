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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1712467378405 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="step_trainer_landing", transformation_ctx="StepTrainerLanding_node1712467378405")

# Script generated for node Customer Curated
CustomerCurated_node1712467414107 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_curated", transformation_ctx="CustomerCurated_node1712467414107")

# Script generated for node SQL Query
SqlQuery0 = '''
SELECT stl.sensorreadingtime
      ,stl.serialnumber
      ,stl.distancefromobject
FROM stl
INNER JOIN cc ON cc.serialnumber = stl.serialnumber
'''
SQLQuery_node1712468913795 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"stl":StepTrainerLanding_node1712467378405, "cc":CustomerCurated_node1712467414107}, transformation_ctx = "SQLQuery_node1712468913795")

# Script generated for node Amazon S3
AmazonS3_node1712467512954 = glueContext.getSink(path="s3://jv-stedi-project/step-trainer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1712467512954")
AmazonS3_node1712467512954.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="step_trainer_trusted")
AmazonS3_node1712467512954.setFormat("glueparquet", compression="snappy")
AmazonS3_node1712467512954.writeFrame(SQLQuery_node1712468913795)
job.commit()
