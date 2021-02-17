import pytest


def func(x):
    return x + 1

# 参数化
@pytest.mark.parametrize('a,b',[
    (1,2),
    (3,4),
    (5,6),
    (11,6),
    ('a1','a2')
])
def test_answer(a,b):
    assert func(a) == b

def test_answer1():
    assert func(4) == 5

@pytest.fixture()
def login():
    print("登录操作")
    usename = 'linfgengzhou'
    return usename

class TestDome:

    def test_a(self,login):
        print(f"a    {login}")
    def test_b(self):
        print("b")
    def test_c(self,login):
        print(f"c    {login}")


if __name__ == '__main__':
    # 方式一，运行指定文件中所有测试类，测试方法
    # pytest.main(["test_a.py"])
    # 方法二，
    pytest.main(["test_a.py::TestDome","-v"])