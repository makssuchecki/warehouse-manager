from src.user import User
import pytest

class TestUser():
    @pytest.fixture
    def make_user(self):
        def make(username, role):
            return User(username, role)
        return make
    
    @pytest.mark.parametrize(
        "username, role, expected",
        [
            ("Kurt Cobain", "admin", "admin"),
            ("James Hetfield", "user", "user"),
            ("Jimmy Hendrix", "mod", "Invalid role"),
        ]
    )
    def test_make_user(self, make_user, username, role, expected):
        user = make_user(username, role)
        assert user.role == expected

    def test_is_admin(self, make_user):
        user = make_user("Courtney Love", "admin")
        result = user.is_admin()
        assert result == True
        
    def test_is_admin_wrong(self, make_user):
        user = make_user("Brian May", "user")
        result = user.is_admin()
        assert result == False
        

