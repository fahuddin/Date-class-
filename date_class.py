#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        self.month = init_month 
        self.day = init_day
        self.year = init_year 
        # add the necessary assignment statements below


    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def advance_one(self):
        """changes the called object so that it represents one calendar day after the date that it originally represented"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        if self.month == 12 and self.day == days_in_month[self.month]:
            self.year += 1 
            self.month = 1
            self.day = 1
        elif self.day == days_in_month[self.month]: 
            self.day = 1 
            self.month += 1 
        else:
            self.day += 1
            
    def advance_n(self, n):
        """changes the calling object so that it represents n calendar days after the date it originally represented"""
        print(self)
        for x in range(n):
            self.advance_one()
            print(self)
            
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) represent the same calendar date"""
        if self.day == other.day:
               if self.month == other.month:
                   if self.year == other.year:
                       return True
        else:
            return False 
    
    def is_before(self, other):
        """True if the called object represents a calendar date that occurs before the calendar date that is represented by other"""
        if  self.year < other.year:
            return True
        elif self.month < other.month and self.year <= other.year:
            return True
        elif self.day < other.day and self.month == other.month and self.year >= other.year:
            return True
        else:
            return False
     
     
    
    def is_after(self,other):
        """True if the calling object represents a calendar date that occurs after the calendar date that is represented by other"""
        if self.year > other.year:
            return True
        elif self.month > other.month and self.year >= other.year:
            return True 
        elif self.day > other.day and self.month == other.month and self.year <= other.year:
            return True 
        else:
            return False 
        
    def days_between(self,other):
        """returns an integer that represents the number of days between self and other"""
        x = self.copy()
        y = other.copy()
        if x == y:
            return 0
        if x.is_before(y) == False:
            count = 0
            while x != y:
                y.advance_one()
                count += 1 
        elif x.is_before(y) == True:
            count = 0
            while x != y:
                x.advance_one()
                count += -1
        return count 
    
    def day_name(self):
        """ returns a string that indicates the name of the day of the week of the Date object that calls it"""
        known_date = Date(11,11,2019)
        day_names = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']
        if self.days_between(known_date) % len(day_names) == 0:
            return day_names[0] 
        elif self.days_between(known_date) % len(day_names) == 1:
            return day_names[1]
        elif self.days_between(known_date) % len(day_names) == 2:
            return day_names[2]
        elif self.days_between(known_date) % len(day_names) == 3:
            return day_names[3]
        elif self.days_between(known_date) % len(day_names) == 4:
            return day_names[4]
        elif self.days_between(known_date) % len(day_names) == 5:
            return day_names[5]
        elif self.days_between(known_date) % len(day_names) == 6:
            return day_names[6]
        
            

        
    
            
        

        
