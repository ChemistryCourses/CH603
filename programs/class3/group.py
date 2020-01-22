import random
team=[]
students=['TIRTHICK MAJUMDER','Namitha Brijit Bejoy','Suryadip Bhattacharjee','Rashmi Arya','Ria Miglani','Ravi Kumar','Rohan Gupta','Tamoghna Mukhopadhyay','Priyam Kumar De','Sneha','Chinmay Sanjay Laxmi Pradhan','Vinayak Sidana','SAWANT SHIVAM LAXMAN','ABHYUDAYA SRIKANT ADULKAR','SUMUKH VAIDYA','YASH GUPTA','VALAY AGARAWAL','YASH BHASKAR','ALOK KUMAR','RONNIE MONDAL','Shruti Tejrao Sose','Prerak Viral Gandhi','Pratik Vasudeo  Kinage','Kshitijkumar Ashok Surjuse','Rohit Auti','Sakshi Gupta','Devesh Singh','Varsha Jain','Niket Kumar Singh','Suraj Sahoo','Rageshwari Ramniklal Marolikar','Ramesh Prasanth Babu']

for i in range(len(students)):
  name=random.choice(students)
  team.append(name)
  students.remove(name)
  if len(team)>2:
    print (team)
    team=[]
print(team)
