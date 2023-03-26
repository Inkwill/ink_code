extends SceneTree

var test = 1
var id = "hahaha"

func _init():
	print("{test} == {id}".format({"test":test,"id":id}))

