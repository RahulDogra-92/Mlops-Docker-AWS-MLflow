from square import square_num

# function and file name should have prefix test_(for unit testing with pytest)
def test_square_num():
    a = 4
    result = square_num(a)
    ##assert the observed value(result) with the expected value
    assert result == 16

