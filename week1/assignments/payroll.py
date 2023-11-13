class Employee:
    def __init__(self, firstName, lastName, employeeID, hourlyWage):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeID = employeeID
        self.hourlyWage = hourlyWage

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

    def setHourlyPay(self, hourlyWage):
        self.hourlyWage = hourlyWage

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
    def getEmployeeID(self):
        return self.employeeID
    
    def __str__(self):
        retStr = self.firstName
        retStr += ""
        retStr = self.lastName
        retStr =+ ""

    def wage(self, hours):
        if (hours <= 40):
            grossWages = hours * self.hourlyWage
            return grossWages
        elif(hours >= 40):
            overTime = ((hours-40)*self.hourlyWage*1.5)+self.hourlyWage*40
            return overTime

empIDNum = int(input("Please enter employee ID number: "))
empFirstName = str(input("Please enter employee's first name: "))
empLastName = str(input("Please enter employee's last name: "))
hourlyWage = float(input("Please enter employee's hourly wage: "))
hoursWorked = float(input("Please enter employee's hours worked: "))
employee = Employee(empIDNum, empFirstName, empLastName, hourlyWage)
pay = employee.wage(hoursWorked)

print(empFirstName + " " + empLastName + "'s wages are " + str(pay))


  

