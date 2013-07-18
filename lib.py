import datetime

def get_formatted_date(date):
	return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%b %d %Y")
	# return str(date)

def get_media_html(resource, type):
	if type == 'image':
		html_resource = "<img src='{0}'/>"
	elif type == 'youtube':
		html_resource = "<p>Youtube video at {0}"
	elif type == 'hyperlink':
		html_resource = "<a href='{0}' target='_blank'>{0}</a>"
	else:
		html_resource = "<p>Unknown media</p>"
	return html_resource.format(resource)