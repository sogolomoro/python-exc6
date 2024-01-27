import re

class User:

    def __init__(self, uid, name, passw):

        self.id = uid

        self.name = name

        self.passw = passw


class Student(User):
    
    def __init__(self, uid, name, passw):
        
        super().__init__(uid, name, passw)
        
        self.courses = set()


class Professor(User):
    
    def __init__(self, uid, name, passw):
    
        super().__init__(uid, name, passw)
        self.coursest = set()


class Course:

    def __init__(self, courseid, name, capacity):

        self.courseid = courseid
        self.name = name
        self.capacity = capacity
        self.current_students = set()


class MainApp:

    def __init__(self):

        self.users = {}
        self.courses = {}
        self.commands = []
        self.poin = 0

    def signup(self, user_type, uid, name, passw):

        
        if user_type!="S" and user_type!= "P":

            
            print  ("invalid type")
            return

        
        if uid.isdigit()==False:
            
            print  ("invalid id")
            return

        
        if " " in name:
            
            print  ("invalid name")
            return
        
        
        if not (4 <= len(passw) <= 20 and any(c in "*!@$%^&()" for c in passw)):
            
            print  ("invalid password")
            return

        
        if uid in self.users.keys():
            
            print ("id already exists")
            return

        
        if user_type == "S":
            
            print ("signed up successfully!")
            self.users[uid] = Student(uid, name, passw)
            return

        
        elif user_type == "P":
            
            print ("signed up successfully!")
            self.users[uid] = Professor(uid, name, passw)
            return


    def login(self, uid, passw):
        
        if uid not in self.users.keys():
            
            print ("incorrect id")
            return

        user = self.users[uid]

        
        if user.passw != passw:
            
            print ("incorrect password")
            return


        
        if isinstance(user, Student):
            
            print ("logged in successfully!\nentered student menu")
            self.smenu(user)

        
        elif isinstance(user, Professor):
            
            print ("logged in successfully!\nentered professor menu")
            self.pmenu(user)

    def smenu(self, student):
        while True:
            self.poin += 1
            command = self.commands[self.poin]

            
            if command == "edu log out edu":
                
                print ("logged out successfully!")
                
                print ("entered log in/sign up menu")
                return

            
            elif command == "edu show course list edu":
                self.clist()

            
            elif command.startswith("edu get course -i "):
                courseid = command.split()[-2]
                self.get_course(student, courseid)

            
            elif command == "edu current menu edu":
                
                print ("student menu")

            else:
                
                print ("invalid command")


    def pmenu(self, professor):
        while True:
            self.poin += 1
            command = self.commands[self.poin]

            
            if command == "edu log out edu":
                
                print ("logged out successfully!")
                
                print ("entered log in/sign up menu")
                return

            
            elif command == "edu show course list edu":
                self.clist()

            
            elif command.startswith("edu add course -c "):

                pattern = re.compile(r'^edu add course -c (.+?) -i (.+?) -n (.+?) edu$')
                match = pattern.match(command)


                
                if match:
                    cname = match.group(1)
                    courseid = match.group(2)
                    capacity = match.group(3)


                else:
                    
                    print ("Invalid command")

                
                if " " in cname:
                    
                    print ("invalid course name")

                
                elif courseid.isdigit()==False:
                    
                    print ("invalid course id")

                
                elif capacity.isdigit()==False:
                    
                    print ("invalid course capacity")

                else:    
                    self.add_course(professor, courseid, cname, capacity)

            
            elif command == "edu current menu edu":
                
                print ("professor menu")
            else:
                
                print ("invalid command")
        
        print ("entered log in/sign up menu")


    def clist(self):
        
        print ("course list:")
        for course in self.courses.values():
            
            print (f"{course.courseid} {course.name} {len(course.current_students)}/{course.capacity}")


    def get_course(self, student, courseid):
        
        if courseid not in self.courses:
            
            print ("incorrect course id")
            return


        course = self.courses[courseid]


        
        if student in course.current_students:
            
            print ("you already have this course")

        
        elif len(course.current_students) >= course.capacity:
            
            print ("course is full")

        else:
            course.current_students.add(student)
            
            print ("course added successfully!")


    def add_course(self, professor, courseid, cname, capacity):

        
        if courseid in self.courses:
            
            print  ("course id already exists")
            return


        self.courses[courseid] = Course(courseid, cname, int(capacity))

        
        print  ("course added successfully!")

    def main(self):
        while True:

            try:
                line = input().strip()
                
                if line == 'edu exit edu':
                    break
                self.commands.append(line)

            except EOFError:
                break

        while True:

            
            if self.poin==len(self.commands):
                break

            command = self.commands[self.poin]

            
            if command == "edu exit edu":
                break

            
            elif command == "edu current menu edu":
                
                print ("log in/sign up menu")

            
            elif command.startswith("edu sign up -"):
                pattern = re.compile(r'^edu sign up -(.+?) -i (.+?) -n (.+?) -p (.+?) edu$')
                match = pattern.match(command)

                
                if match:
                    user_type = match.group(1)
                    uid = match.group(2)
                    name = match.group(3)
                    passw = match.group(4)

                else :
                    
                    print ("invalid command")
                    self.poin += 1
                    continue

                self.signup(user_type, uid, name, passw)

            
            elif command.startswith("edu log in -"):
                pattern = re.compile(r'^edu log in -i (.+?) -p (.+?) edu$')
                match = pattern.match(command)

                
                if match:
                    uid = match.group(1)
                    passw = match.group(2)
                 
                else:
                    
                    print ("invalid command")
                    self.poin += 1
                    continue

                self.login(uid, passw)
            else:
                
                print ("invalid  command")
            self.poin += 1



if __name__ == "__main__":
    app = MainApp()
    app.main()