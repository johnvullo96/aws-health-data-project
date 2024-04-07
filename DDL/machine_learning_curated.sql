CREATE EXTERNAL TABLE `machine_learning_curated`(
  `sensorreadingtime` bigint, 
  `serialnumber` string, 
  `distancefromobject` int, 
  `user_acc` string, 
  `x` double, 
  `y` double, 
  `z` double)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://jv-stedi-project/step-trainer/curated/'
TBLPROPERTIES (
  'CreatedByJob'='STEDI_Machine Learning Curated', 
  'CreatedByJobRun'='jr_cceed1ae98378bb75eeec4a7f0365aeb384320ff714c539d3b4a32d67abb0296', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
