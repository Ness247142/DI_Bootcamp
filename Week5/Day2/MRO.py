# OOP: MRO - Method Resolution Order (Inheritance Algorithm)

#Example 1
class A:
	num = 10

class B(A):
	pass

class C(A):
	num = 1

class D(B,C):
	pass

print(D.mro())
D.num

# Output
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]


#Example 2
class X: pass
class Y: pass
class Z: pass
class A(X,Y): pass
class B(Y,Z): pass
class M(B,A,Z): pass

print(M.__mro__)

# Output
# (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>)

