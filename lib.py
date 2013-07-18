import datetime
import urllib2

def get_date_sticker(year):
	return '<div class="event event-box sticker">%s</div>' % year

def get_formatted_date(date):
	return datetime.datetime.strptime(date, "%Y-%m-%d")

def get_media_html(resource, type):
	if type == 'image':
		html_resource = "<img src='{0}'/>"
	elif type == 'youtube':
		youtube_id = resource.split('v=', 1)[1]
		resource = youtube_id
		html_resource = "<iframe src='//www.youtube.com/embed/{0}' frameborder='0' allowfullscreen></iframe>"
	elif type == 'hyperlink':
		# req = urllib2.Request(resource)
		# res = urllib2.urlopen(req)
		# img = '<img' + res.read().split('<img',1)[1].split('>')[0] + '/>'
		# if int(img.split("height='", 1)[1].split("'")[0]) < 50:
		# 	html_resource = "<a href='{0}' target='_blank'>{0}</a>"
		# else:
		# html_resource = "<a href='{0}' target='_blank'>"+img+"</a><a href='{0}' target='_blank'>{0}</a>"
		html_resource = "<a href='{0}' target='_blank'>{0}</a>"
	else:
		html_resource = "<p>Unknown media</p>"
	return html_resource.format(resource)