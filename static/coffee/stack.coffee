$ ->
	buildColumns()
	setHeights()
	setWidths()

##########################
# LAYOUT FUNCTIONS
##########################

setWidths = () ->
	event_width = $("#container").width()/2 - 20
	$(".event-box").width(event_width)

setHeights = () ->
	container_H = $("#container").height()
	container_OH = $("#container").outerHeight()
	container_IH = $("#container").innerHeight()
	header_OH = $("header").outerHeight()
	timeline_vr_height = container_H + (container_OH - container_H)/2 + header_OH
	$(".timeline-vr").height(timeline_vr_height)

buildColumns = () ->
	left_column_height = 0
	right_column_height = 0
	events = $(".event-box")
	i = 0

	while i < events.length
	  events.eq(i).height Math.floor(Math.random() * 400 + 200)
	  
	  if left_column_height > right_column_height
	    right_column_height += events.eq(i).removeClass("left").addClass("right").outerHeight(true)
	  else
	    left_column_height += events.eq(i).removeClass("right").addClass("left").outerHeight(true)
	  i++