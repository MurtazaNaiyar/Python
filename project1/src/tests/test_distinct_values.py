from pyspark.sql import SparkSession
from utils.distinct_values import get_distinct_values


def spark_session():
    """Fixture for creating a spark context."""
    return SparkSession.builder. \
        appName("pyspark-test"). \
        getOrCreate()


def test_get_distinct_values():
    spark = spark_session()
    mock_data: list = [('X', 'Annual'), ('Y', 'Daily')]
    expected_result: list = ['Annual', 'Daily']
    schema: list = ['A', 'B']

    mock_df = spark.createDataFrame(data=mock_data, schema=schema)
    assert get_distinct_values(df=mock_df, column='B') == expected_result
