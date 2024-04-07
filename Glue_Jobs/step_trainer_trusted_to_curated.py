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

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1712466669353 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="step_trainer_trusted", transformation_ctx="StepTrainerTrusted_node1712466669353")

# Script generated for node Customer Curated
CustomerCurated_node1712470047253 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="customer_curated", transformation_ctx="CustomerCurated_node1712470047253")

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1712466683770 = glueContext.create_dynamic_frame.from_catalog(database="stedi-project", table_name="accelerometer_trusted", transformation_ctx="AccelerometerTrusted_node1712466683770")

# Script generated for node SQL Query
SqlQuery0 = '''
select  
        stt.sensorreadingtime
       ,stt.serialnumber
       ,stt.distancefromobject
       ,acct.user_acc
       ,acct.x
       ,acct.y
       ,acct.z
from stt
LEFT JOIN cc ON cc.serialnumber = stt.serialnumber
INNER JOIN acct ON acct.timestamp_acc = stt.sensorreadingtime
'''
SQLQuery_node1712469442007 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"stt":StepTrainerTrusted_node1712466669353, "acct":AccelerometerTrusted_node1712466683770, "cc":CustomerCurated_node1712470047253}, transformation_ctx = "SQLQuery_node1712469442007")

# Script generated for node Amazon S3 - Machine Learning Curated
AmazonS3MachineLearningCurated_node1712469570921 = glueContext.getSink(path="s3://jv-stedi-project/step-trainer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3MachineLearningCurated_node1712469570921")
AmazonS3MachineLearningCurated_node1712469570921.setCatalogInfo(catalogDatabase="stedi-project",catalogTableName="machine_learning_curated")
AmazonS3MachineLearningCurated_node1712469570921.setFormat("glueparquet", compression="snappy")
AmazonS3MachineLearningCurated_node1712469570921.writeFrame(SQLQuery_node1712469442007)
job.commit()
