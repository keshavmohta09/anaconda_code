import pandas as pd
import sqlalchemy
engine = sqlalchemy.create_engine('mysql+pymysql://root:q1w2e3r4@localhost:3306/test1')
# df = pd.read_sql_table("studentmanager",engine)
# df = pd.read_sql_query("select * from studentmanager",engine)
# df = pd.read_sql_query('describe studentmanager',engine)
try:
    # qry = '''
    # create table basicdetails(
    # s_no int not null auto_increment,
    # full_name varchar(100) not null,
    # phone bigint not null,
    # email varchar(100),
    # primary key (s_no)
    # );

    # drop table basichumandetails;
    # '''

    # qry = '''
    # insert into basicdetails
    # (full_name,phone,email)
    # values
    # ('Shubham Mohta',8869006058,'shubhammohta09@gmail.com'),
    # ('Keshav Mohta',9027669897,'keshavmohta09@gmail.com'),
    # ('Rajendra Mohta',9720197952,'rajendramohta09@gmail.com');
    # '''

    # df = pd.read_sql_query(qry,engine)
    df = pd.read_sql_table('basicdetails',engine)
    print(df)
except Exception as e:
    print(e)