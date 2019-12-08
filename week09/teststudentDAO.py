from studentDAO import studentDAO

#create
latestid = studentDAO.create(('Mark', 45))
#find by ID
result = studentDAO.findByID(latestid);
print(result)

#update
studentDAO.update(('Fred', 21, latestid))
result = studentDAO.findByID(latestid);
print(result)

#get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

#delete
studentDAO.delete(latestid)