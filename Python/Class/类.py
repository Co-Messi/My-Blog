class ClassA():
    var1 = '两点水'

    @classmethod
    def fun1(cls):
        print('原来的 var1 值为：' + cls.var1)
        cls.var1 = input('请输入修改 var1 的值：')
        print('修改后 var1 值为: '+ cls.var1)
        cls.var2 = input('新曾类属性 var2, 请为它赋值为：')
        print('修改后 var2 值为：'+ cls.var2)


ClassA.fun1()   