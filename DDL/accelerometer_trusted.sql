CREATE EXTERNAL TABLE `accelerometer_trusted`(
  `user_acc` string, 
  `timestamp_acc` bigint, 
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
  's3://jv-stedi-project/accelerometer/trusted/'
TBLPROPERTIES (
  'CreatedByJob'='STEDI_Accelerometer Landing to Trusted', 
  'CreatedByJobRun'='jr_1de0ea225c97eea2aa975b0b1a868acc521487aeda933d554a91bfb27497b99f', 
  'classification'='parquet', 
  'useGlueParquetWriter'='true')
