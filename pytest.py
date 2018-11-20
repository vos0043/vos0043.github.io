import rekenmachine as rm

def test_add(x,y):
    if (rm.add(x,y) == x + y):
        return True
    else:
        return False

def test_subtract(x,y):   
    if (rm.subtract(x,y) == x - y):
        return True
    else:
        return False
    
def test_multiply(x,y):
    if (rm.multiply(x,y) == x * y):
        return True
    else:
        return False
    
def test_divide(x,y):
    if (rm.divide(x,y) == x / y):
        return True

    else:
        return False
		
def test_all(x,y):
	if test_add and test_divide and test_subtract and test_multiply:
		return 0
	else:
		return 1
		
test_all(10,5)