CREATE EXTERNAL TABLE `step_trainer_trusted`(
  `sensorreadingtime` bigint, 
  `serialnumber` string, 
  `distancefromobject` int)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://jv-stedi-project/step-trainer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='STEDI_Step Trainer Trusted2', 
  'CreatedByJobRun'='jr_8ca90f2b6a289ddcafc5bae6720df92d6f9a2c734338de6f9570c04df82a30b0', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
