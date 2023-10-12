# Databricks notebook source
# MAGIC %sh
# MAGIC ls

# COMMAND ----------

# MAGIC %pip install dbt-redshift

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %sh
# MAGIC dbt deps

# COMMAND ----------

# MAGIC %sh
# MAGIC dbt seed

# COMMAND ----------

# MAGIC %sh
# MAGIC dbt run

# COMMAND ----------


