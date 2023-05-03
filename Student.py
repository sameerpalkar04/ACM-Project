#ACM PROJECT
import mysql.connector
import webbrowser
mydb=mysql.connector.connect(host="localhost",user="root",passwd="s@meer2004",database="acm")
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM student_info;')
data = mycursor.fetchall() 
p = []
for row in data:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b = "<td>%s</td>"%row[1]
    p.append(b)
    c = "<td>%s</td>"%row[2]
    p.append(c)
    d = "<td>%s</td>"%row[3]
    p.append(d)
    d = "<td>%s</td>"%row[4]
    p.append(d)
    e = "<td>%s</td>"%row[5]
    p.append(e)
    f = "<td>%s</td>"%row[6]
    p.append(f)
    g = "<td>%s</td>"%row[7]
    p.append(g)
    h = "<td>%s</td></tr>"%row[8]
    p.append(h)
contents = '''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width-device-width, initial-scale=1">
<title>ACM PROJECT</title>
<style>
table, th, td {
    border: 3px solid black;
    border-collapse: collapse;
}
table.center {
    margin-left: auto;
    margin-right:auto;
}
</style>
</head>
<body style="background-color:black;">
<h1 style="color:green;text-align:center;font-family:courier new;font-size:55px"><u><b> STUDENT INFORMATION </b></u></h1>
<h2 style="color:green">================================================================================================================</h2>
<table bgcolor="lightgrey"; class="center">
<tr bgcolor="grey">
    <th>SNo</th>
    <th>Name</th>
    <th>Age</th>
    <th>Father Name</th>
    <th>Phone Number</th>
    <th>Blood Group</th>
    <th>Weight</th>
    <th>Height</th>
    <th>Gender</th>
</tr>
%s
</table>
<h4 style="color:white;text-align:center;font-family:georgia"> Made by: Sameer Satyajit Palkar </h4>
<h4 style="color:white;text-align:center;font-family:georgia"> Registration Number: 22BCE3037 </h4>
<h2 style="color:green">================================================================================================================</h2>
</body>
</html>
'''%(p)

filename = 'studentinfo.html'
#function to write the contents of the table
def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)
mydb.close()
