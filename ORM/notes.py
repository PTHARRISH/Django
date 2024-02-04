# RDBMS
# Relational database management system will provide the tools to build and manage our database system 
# include MySQL,PostgreSQL.
# There are many more how ever Mysql and PostgreSQL are generally the top of any popularity list
# With in our RDBMS Software we construct or build databases now.
# RDBMS can manage multiple databases.
# In Django we just have the one database. 
# Database is a container we logically organize tables and establish relationships
# In our project may have five or ten tables
# tables stores data logically in rows and fields

# What is realtional database
# A relational database is a type of database that organizes data into tables, 
# which are composed of rows and columns. 
# Each row represents a record of data, and each column represents a field or attribute of data. 
# Tables can be linked together by common fields, called keys, to show the relationships between data. 
# Users can query the database using SQL, a language for manipulating and retrieving data


# Traditional Approach:
# 1) 3rd Party Software GUI: Softwares to connect our RDBMS and use that interface of the software

# all() Query
# It is used to display all the values in the database

# filter() :
# It is used to filter and display the particular condition
# Inside the filter 
# filter(firstname=name)
# filter(firstname__startswith=name)
# filter(lastname__endswith=name)

# Simple OR Query
# OR query is used for there are two set of queries if either one condition becomes True 
# it prints the output query 
# OR is a logical operator that retrieves records satisfying either of the specified conditions.
# OR queries in Django are used to filter records that match any of the specified conditions.

# Student_E.objects.filter(lastname__startswith="PT") | Student_E.objects.filter(lastname__endswith="Admin")
# <QuerySet [<Student_E: Unknown>, <Student_E: main>]>
# 
# ID	Full Name	    Age	    Class	    Teacher name
# 2	    Unknown PT	    23	    II year	    Brook
# 3	    main Admin	    18	    I Year	    Luffy


# Q objects
# A Q object in Django is a container for keyword arguments that can be used 
# to create complex queries involving logical operators such as AND, OR, and NOT. 
# You can import Q objects from django.db.models and use them with query methods such as filter, exclude, or get.