#coding=utf-8

def dump(expression):
    result=eval(expression)
    print expression, "---->",result,type(result)


dump("1")
dump("1.03")
dump("'allbit'")
dump("1.0+2.0")
dump("'@'*2")
dump("len('ablc')")
dump("len('ablc')+233")

print eval("__import__('os').getcwd()")


    
