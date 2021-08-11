def test(year: int):
        if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
            print('{0} 是闰年' .format(year))
        else:
            print('{0} 不是闰年' .format(year))

if __name__=="__main__":
        test(2012)