extends Node2D

var color: Color
var weight: float = 1
var deletable: bool = true

func _ready():
	set_process( true )
	color = Color.from_hsv( randf(), 1.0, 1.0 )

func get_len(v):
	return sqrt( v.x**2 + v.y**2 )

func _process(delta):
	deletable = true
	queue_redraw()
	var sum: Vector2 = Vector2( 0, 0 )
	var speed = ProjectSettings.get_setting("global/speed")
	for node in get_parent().get_children( false ):
		var vec = Vector2( node.position.x - position.x, node.position.y - position.y )
		sum += (node.weight / weight) * speed * vec / maxf( vec.length_squared(), 1 )
	position += sum

func _draw():
	draw_circle( position, 10 * weight, color )
	for node in get_parent().get_children( false ):
		draw_line( position, node.position, color, 0.5, true )
