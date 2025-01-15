class Shift():

    def __init__(self, date, role, start_time, end_time):
        self.date = date
        self.role = role
        self.start_time = start_time
        self.end_time = end_time
    
    def get_date(self):
        return self.date
    
    def get_role(self):
        return self.role
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def to_dict(self):
        return {
            'date': self.date,
            'role': self.role,
            'start_time': self.start_time,
            'end_time': self.end_time
        }
    