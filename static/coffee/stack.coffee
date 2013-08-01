$ ->
	buildColumns()
	setHeights()
	setWidths()
	setInitialInput()
	checkInputs()

##########################
# LAYOUT FUNCTIONS
##########################

setWidths = () ->
	event_width = $("#container").width()/2 - 20
	$(".event-box").width(event_width)
	timeline_vr_width = $(".timeline-vr").outerWidth()
	timeline_vr_pos = $(".timeline-vr").css("left")
	$(".timeline-vr").css("left", parseInt(timeline_vr_pos, 10) - timeline_vr_width/2)

setHeights = () ->
	container_H = $("#container").height()
	container_OH = $("#container").outerHeight()
	timeline_vr_height = container_H + (container_OH - container_H)/2
	$(".timeline-vr").height(timeline_vr_height)

buildColumns = () ->
	left_column_height = 0
	right_column_height = 0
	events = $(".event-box")
	i = 0

	while i < events.length
	  if left_column_height > right_column_height
	    right_column_height += events.eq(i).removeClass("left").addClass("right").outerHeight(true)
	  else
	    left_column_height += events.eq(i).removeClass("right").addClass("left").outerHeight(true)
	  i++

##########################
# INPUT FUNCTIONS
##########################

setInitialInput = () ->
	$("i.icon-camera-retro").addClass('icon-selected')
	$("input[name='media_type']").val('image')

checkInputs = () ->
	$("#icon-options i").click ->
		$("#icon-options i").removeClass('icon-selected')
		$(this).addClass('icon-selected')
		if $(this).hasClass('icon-camera-retro')
			$("input[name='media_type']").val('image')
		if $(this).hasClass('icon-youtube')
			$("input[name='media_type']").val('youtube')
		if $(this).hasClass('icon-link')
			$("input[name='media_type']").val('hyperlink')