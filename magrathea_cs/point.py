from math import sqrt

class Point:
	def __init__( A, x, y, w = 1.0 ):
		A.x, A.y, A.w = float( x ), float( y ), float( w )
	def __add__( A, B ):
		return Point( A.x + B.x, A.y + B.y )
	def __sub__( A, B ):
		return Point( A.x - B.x, A.y - B.y )
	def __iadd__( A, B ):
		A.x += B.x
		A.y += B.y
	def __isub__( A, B ):
		A.x -= B.x
		A.y -= B.y
	def __mul__( A, β ):
		return Point( A.x * β, A.y * β )
	def __truediv__( A, β ):
		return Point( A.x / β, A.y / β )
	def len( A ):
		return sqrt( A.x**2 + A.y**2 )
	def len_sqr( A ):
		return A.x**2 + A.y**2
	def __repr__( A ):
		return "Point( {}, {}, w = {} )".format( round( A.x, 2 ), round( A.y, 2 ), A.w )
	def __str__( A ):
		return "Point( {}, {}, w = {} )".format( round( A.x, 2 ), round( A.y, 2 ), A.w )
	