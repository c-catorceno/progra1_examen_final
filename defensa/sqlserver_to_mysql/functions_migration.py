from sqlserver_to_mysql.query import other_properties

def get_schema(table_name, old_c) -> list[tuple]:
    old_c.execute(f"""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table_name}'
    """)
    columns = old_c.fetchall()
    return columns

def create_tables(table_name, columns, new_c) -> None:
    create_table_query : str = f"CREATE TABLE {table_name} ("
    column_properties : list[str] = []
    column_properties = define_columns(columns, column_properties)
    create_table_query += ", ".join(column_properties) + ");"
    new_c.execute(create_table_query)

def define_columns(columns, column_properties) -> list[str]:
    for column in columns:
        column_name, data_type = column 
        if data_type in ["nvarchar", "varchar"]:
            data_type = "VARCHAR(50)"
        else: data_type = data_type 
        column_properties.append(f"{column_name} {data_type}")
    return column_properties

def migrate_records(table_name, columns, old_c, new_c):
    old_c.execute(f"SELECT * FROM  {table_name};")
    rows = old_c.fetchall()
    if rows:
        placeholders = ", ".join(["%s"] * len(columns))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
        for row in rows:
            new_c.execute(insert_query, tuple(row))

def get_relations(new_c) -> None:
    sql_script = other_properties()
    for statement in sql_script.split(';'):
        if statement.strip():
            new_c.execute(statement + ';')
