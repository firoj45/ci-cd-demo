def test_addition():
    assert 2 + 2 == 4   # ✅ pass

def test_string():
    assert "hello".upper() == "HELLO"   # ✅ pass

def test_list_length():
    assert len([1, 2, 3]) == 3   # ✅ pass

def test_fail_math():
    assert 5 * 2 == 11   # ❌ fail (actual is 10)

def test_fail_string():
    assert "python".capitalize() == "PYTHON"   # ❌ fail (actual is "Python")
