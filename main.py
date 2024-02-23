from threading import Thread

#ТЕСТЫ
def test_recursion():
    result = '1 -> 2 -> 3 -> 4 -> 5 -> None'
    lst = recursion(([1, [2, [3, 4, [5]]]]))
    _ = ''
    for i in lst:_ += str(i) + " -> "
    _ += "None"
    assert result == _

def test_no_recursion():
    result = '1 -> 2 -> 3 -> 4 -> 5 -> None'
    lst = no_recursion(([1, [2, [3, 4, [5]]]]))
    _ = ''
    for i in lst:_ += str(i) + " -> "
    _ += "None"
    assert result == _

def test_recursion_21():
    assert recursion2(1) == no_recursion2(1)
def test_recursion_22():
    assert recursion2(2) == no_recursion2(2)
def test_recursion_23():
    assert recursion2(3) == no_recursion2(3)
def test_recursion_24():
    assert recursion2(4) == no_recursion2(4)
def test_recursion_25():
    assert recursion2(5) == no_recursion2(5)

#ЗАДАНИЕ 1
def recursion(lst):
    res = []
    for item in lst:
        if isinstance(item, list):
            res.extend(recursion(item))
        else:
            res.append(item)
    return res

def no_recursion(lst):
    lst1 = [lst]
    res = []
    while lst1:
        last = lst1.pop()
        for _ in last:
            if isinstance(_, list):
                lst1.append(_)
            else:
                res.append(_)
    return res

#ЗАДАНИЕ 2
def recursion2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return recursion2(n - 2) + recursion2(n - 1) / (2 ** (n - 1))

def no_recursion2(n):
    a = [1, 1]
    for i in range(2, n + 1):
        a.append(a[i - 2] + a[i - 1] / (2 ** (i - 1)))
    return a[n]

#print(" -> ".join(map(str, recursion(([1, [2, [3, 4, [5]]]])))),'-> None')
#print(" -> ".join(map(str, no_recursion(([1, [2, [3, 4, [5]]]])))),'-> None')