from app import start

def test_start():
    """Test app start"""
    assert start() == True, "Start should return true"