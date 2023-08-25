# Importing required libraries
import os
import Config
import psycopg2

# Number of rows counter
id_log = 1

# Connection to the database
conn = psycopg2.connect(
    database=Config.database,
    user=Config.user,
    password=Config.password,
    host=Config.host,
    port=Config.port
)

# Enabling automatic commits
conn.autocommit = True

# cursor creation
cursor = conn.cursor()

# file scan
for r, s, f in os.walk(Config.pathLog):
    for i in range(len(f)):
        print(f[i])
        # Leitura de arquivos
        with open(f"{r}/{f[i]}", "r", encoding="UTF-8") as txt:
            # file reading
            log = txt.readlines()
            for content in log:
                # Check if the read line is a comment
                if content[0][0] == "#":
                    continue
                else:
                    # Turns the read line into a list
                    content = content.split()

                    # Creates SQL command for inserting the contents of the rows in the database
                    sql = f'''insert into {Config.tabel} values('{id_log}','{content[0]} {content[1]}', '{content[0]}',
                    '{content[1]}','{content[2]}','{content[3]}', '{content[4].replace("'", "''")}',
                    '{content[5].replace("'", "''")}', '{content[6]}', 
                    '{content[7].replace("'", "''")}', '{content[8]}', '{content[9].replace("'", "''")}', 
                    '{content[10].replace("'", "''")}', '{content[11]}', '{content[12]}', '{content[13]}', 
                    '{content[14]}');'''

                    # Try to run the SQL command
                    try:
                        # Run the SQL command
                        cursor.execute(sql)

                    # Handles the Primary Key violation error
                    except psycopg2.errors.UniqueViolation as U:
                        print('duplicate log_id: {}'.format(id_log))

                    # Handles possible "generic" errors
                    except Exception as e:
                        print(f"{sql} ERROR -> {e}")

                    # Handles forced program interruption
                    except KeyboardInterrupt:
                        # Commit the data to the database and close the connection
                        conn.commit()
                        conn.close()

                    finally:
                        # Increments the number of rows
                        id_log += 1

    print("\n=====-----=====")

# Commit the data to the database and close the connection
conn.commit()
conn.close()

# Closes the program
print("Done! :)")
