# Assignment - 28 Full Stack Web Development using Python MySirG

# Postgres DB

# 1. Create a table (student) with 3 columns (rollno, name, course).

#query 
# create table student(rollno int, name text, course text);



# 2. Insert records for 4 students.


# insert data in table 
#record number one
#insert into student values(1,'Rohit','Python');

#record number two
# insert into student values(2,'Diwaker','Java');

# record number three.

# insert into student values(3,'Ritesh','Javascript');
#record number four
#insert into student values(4,'Shivam','C#');



# 3. Write a Select query to fetch all the students.

# select rollno from student;

# select * from student;


# 4. Update the student name of rollno 3 with ‘Mohan’

# update student set  rollno=3 where name='Mohan';


# 5. Delete any student from table with their rollno.

# delete student where rollno=xyz;



# 6. Delete all the data from student table.

# delete student table;

# 7. Drop the student table.

# drop student ;

# 8. Create Courses table (cid, cname) where cid is a primary key and Student table
# (rollno, name, cid) where rollno is a primary key and cid is a foreign key.


# create table courses ( cid int, cname text);
# create table student (rollno int,name text, cid int primary key(cid),constraint fk_cid foreign key(cid)
# references courses(cid));




# 9. Insert data in both the tables.

# insert into student values(101,'Diwaker',1);
# insert into student values(102,'Maxwell',2);
# insert into student values(103,'Allen_Turing',3);


# 10. Select all the students who are doing a specific course, eg. Python.

# select name from student where cid in(select cid from cid where cname='python');
