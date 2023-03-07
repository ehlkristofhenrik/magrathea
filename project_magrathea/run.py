import main

# Main

points = np.array([
    [ 1, 5 ],
    [ 2, 10 ],
    [ 3, 15 ]
], dtype=np.float64 )

from random import uniform

points = np.array( [ [ x, x * 2 + 1 ] for x in range( 10 ) ], dtype = np.float32 )

weight = np.array( [ 1 for x in range( 10 ) ], dtype = np.float32 )

N = len( points ) // 2
L = len( points )

left = points[:N]
right = points[L-N:]

left_w = weight[:N]
right_w = weight[L-N:]

while len( left ) > 1 or len( right ) > 1:
    left, left_w = gravitate( left, left_w )
    right, right_w = gravitate(right, right_w)

print( line( left[0], right[0] ) )

px.scatter( points, 0, 1 ).show()

arr = np.array([
    left,
    right
]).reshape( ( 2, 2 ) )

print( arr )

px.line( arr, 0, 1 ).show()