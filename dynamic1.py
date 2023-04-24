def fun2(n):
    if n<=5:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)
    print(n)
fun2(8)