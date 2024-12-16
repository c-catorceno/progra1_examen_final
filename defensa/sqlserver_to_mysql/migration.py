from connections import *
from functions_migration import *

sqlserver = connect_sqlserver()
old_c = sqlserver.cursor()
try:
    mysqll = connect_mysqll()
    new_c = mysqll.cursor()

    db_name = "Gym_migrado"
    new_c.execute(f"SHOW DATABASES LIKE '{db_name}';")
    if new_c.fetchone():
        print(f"La base de datos '{db_name} ya existe. La migración ya fue realizada.'")
        exit()
    new_c.execute(f"CREATE DATABASE {db_name};")
    new_c.execute(f"USE {db_name};")

    tables = ["CLIENTE", "SERVICIO", "INSCRIPCION", "PAGOS", "ASISTENCIA", "ENTRENADORES"]
    for table_name in tables:
        print(f"Migrando tabla: {table_name}")
        columns = get_schema(table_name, old_c)
        create_tables(table_name, columns, new_c)
        migrate_records(table_name, columns, old_c, new_c)
        mysqll.commit()
        print(f"Tabla {table_name} migrada exitosamente.")

    print("Aplicando modificaciones adicionales...")
    get_relations(new_c)
    mysqll.commit()
    print("Modificaciones aplicadas exitosamente.")

except Error as e:
    print(f"Error en la conexión o migración: {e}")

finally:
    if sqlserver:
        old_c.close()
        sqlserver.close()
    if mysqll.is_connected():
        new_c.close()
        mysqll.close()
