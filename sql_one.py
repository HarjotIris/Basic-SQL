from google.cloud import bigquery
# create a client object
client = bigquery.Client()

# creating a refernce to the "hacker-news" dataset
dataset_ref = client.dataset("hacker-news", project = "bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# list all the tables in the "hacker-news" dataset
tables = list(client.list_tables(dataset))

# print the names of all the tables in the dataset
for table in tables:
    print(table.table_id)

# construct a reference to the full table
table_ref = dataset_ref.table("full")

# API request - fetch the table
table = client.get_table(table_ref)

# print info on all the columns in the "full" table in the "hacker-news" dataset
table.schema

# preview the first five lines of the "full" table
client.list_rows(table, max_results=5).to_dataframe()

# preview the first 5 entries in the "by" column of the "full" table
client.list_rows(table, selected_fields=table.schema[:1], 
                 max_results=5).to_dataframe()