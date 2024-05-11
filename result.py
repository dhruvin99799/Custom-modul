class result():
    def exam(s):
        player = dict()
        n=int(input("Enter Number Of Students= "))
        for i in range(n):
            name=(input("Enter Student Name = "))
            marks=[]
            n1=int(input("Enter Subjects Of Students= "))
            for i in range(n1):
                mark = int(input("Enter Marks = "))
                marks.append(mark)
            player[name] = marks
            t_marks=sum(marks)
            print("Total Marks = ",t_marks)
            avrage=t_marks/n1
            print("Student Avrage For Exam = ",avrage)
            print("MinMum Marks Of All Exam = ",min(marks))
            print("Maximum Marks Of All Exam = ",max(marks))       
            if(avrage>90):
                print("Grade = A1")
            elif(avrage>80):
                print("Grade = A2")
            elif(avrage>70):
                print("Grade = B1")
            elif(avrage>60):
                print("Grade = B2")
            elif(avrage>50):
                print("Grade = C1")
            elif(avrage>40):
                print("Grade = C2")
            elif(avrage>35):
                print("Grade = D")
            else:
                print("Grade = -----")
         
            # a = open('resout.txt','w')
            # print(a.write(str(name)))
obj = result()
obj.exam()