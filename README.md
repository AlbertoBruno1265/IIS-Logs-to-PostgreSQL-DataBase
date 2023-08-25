# IIS-Logs-to-PostgreSQL-DataBase

## Abstract
 IIS log reader with Postgre database recording.

 ## Requeriments
 - Python 3.6 or >
 - psycopg2 2.9.7

## Log Format

![Log_format.png](https://github.com/AlbertoBruno1265/IIS-Logs-to-PostgreSQL-DataBase/blob/main/imgs/Log_format.png)
 
## Settings
To configure the program, access "[Config.py](https://github.com/AlbertoBruno1265/IIS-Logs-to-PostgreSQL-DataBase/blob/main/pyFiles/Config.py)", then put the parameters inside the " "

![Settings](https://github.com/AlbertoBruno1265/IIS-Logs-to-PostgreSQL-DataBase/blob/main/imgs/Settings.png)

| **Parameter** | **Description**
| :--------------- | :-----------------
| database | Name of PostgreSQL Database
| user     | Database owner username
| password | Owner user password
| host     | Database ip address
| port     | Ip address port
| table    | Name of tabel
| pathLog  | Path to .log files

## My LinkedIn
Click [here](https://www.linkedin.com/in/alberto-bruno-silvestre-de-oliveira-b7a010259/) to acesse my LinkedIn
