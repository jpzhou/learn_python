# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:
# Author:      jp $
# -------------------------------------------------------------------------------
from pyspark.sql.types import BooleanType, Row
from pyspark import SQLContext, SparkContext
sc = SparkContext()
sqlContext = SQLContext()


def check_only_contain_chinese(check_str):
    for ch in check_str.strip():
        if not u'\u4e00' <= ch <= u'\u9fa5':
            return False
    return True

sqlContext.registerFunction('check_only_contain_chinese', check_only_contain_chinese, BooleanType())

# load text data
line = sc.textFile("/tmp/test_person_score.txt")
parts = line.map(lambda l: l.split())
people = parts.map(lambda p: Row(name=p[0], phone=p[1]))
schemaPeople = sqlContext.createDataFrame(people)

# write text data
schemaPeople.write.text('/tmp/test_person_score_txt')

# create empty dataFrame from schema
emptySchema = sqlContext.createDataFrame([], schemaPeople.schema)
emptySchema.registerTempTable('emptySchemaTable')
sqlContext.sql('create table db_name.tb_name partitioned by (batch_id STRING) as select * from emptySchemaTable')




