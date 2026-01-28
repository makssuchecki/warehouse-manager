
class User:
    def __init__(self, username, role):
        self.username = username
        if role in ("admin", "user"):
            self.role = role
        else:
            self.role = "Invalid role"
            
    def is_admin(self):
        return self.role == "admin"
    
