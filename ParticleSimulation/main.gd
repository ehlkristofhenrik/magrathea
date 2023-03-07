extends Control

var scn = preload("res://point.tscn")

func on_slider_value_changed(value):
	ProjectSettings.set_setting("global/speed", value)

func _process(_delta):
	if Input.is_action_just_pressed("click"):
		var ins = scn.instantiate()
		ins.set_global_position( get_global_mouse_position() / 2 )
		$Points.add_child(ins)
	for p1 in $Points.get_children():
		for p2 in $Points.get_children():
			if p1 != p2 and p1.deletable and p1.position.distance_to(p2.position) <= (p1.weight * p2.weight) * $UI/Beta.value:
				p1.queue_free()
				p2.weight += p1.weight + $UI/Gamma.value
				p2.deletable = false

func slide(value):
	ProjectSettings.set_setting("global/speed", value / 2)

func _on_minimize_pressed():
	for i in $Points.get_children():
		i.weight = 1
