import platform
import pypyodbc
import pandas as pd
import os

con = pypyodbc.connect(
    '''
    Driver={SQL Server};
    Server=serverName;
    Database=databaseName;
    UID=userName;
    PWD=password;
    '''
)

pcos = platform.system() #İşletim sistemini gösterir.
processor = platform.processor() #İşlemci bilgisini gösterir.
pythonver = platform.python_version() #Python versiyonunu gösterir.
pcuser = platform.node() #Bilgisayarın kullanıcı adını gösterir.
pycompiler = platform.python_compiler() #Python compiler verisini gösterir.
pyimplementation = platform.python_implementation() #Python implementation bilgisini gösterir.

cursor = con.cursor()

cursor.execute(
    '''
    create table pc(
        os nvarchar(25) not null,
        processor text not null,
        pythonver text not null,
        pcuser text not null,
        pycompiler nvarchar(50) not null,
        pyimplementation text not null,
    )
    '''
)

cursor.execute(
    f'''
    insert into pc(os,processor,pythonver,pcuser,pycompiler,pyimplementation)
    values ('{pcos}','{processor}','{pythonver}','{pcuser}','{pycompiler}','{pyimplementation}')
    '''
)

con.commit()

cursor.execute('select * from pc')
table = cursor.fetchall()

os.chdir(r'C:\Users\user\Desktop')
os.mkdir('pc')

df = pd.DataFrame(table)
df.to_csv (r'C:\Users\user\Desktop\pc\properties.csv', index = False)
