from django.http import JsonResponse
from django.shortcuts import render
from . models import page
from django.views.generic import View
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px

x_data = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y_data = [x**0.5 for x in x_data]
plot_div1 = plot([Scatter(x=x_data, y=y_data,
					mode='lines', name='test',
					opacity=0.8, marker_color='green')],
			output_type='div')
plot_div2 = plot([Scatter(x=y_data, y=x_data,
					mode='lines', name='test2',
					opacity=0.8, marker_color='blue')],
			output_type='div')

def index(request, pagename):
	pagename = '/' + pagename
	pg = page.objects.get(permalink=pagename)
	if pagename=='/':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			}
	if pagename=='/about':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			}
	if pagename=='/coldwatert':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			}
	if pagename=='/coldwaterp':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			'plot_div': plot_div1,
			}
	if pagename=='/utilization':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			}
	if pagename=='/machinevibe':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			}
	if pagename=='/enclosetemp':
		context = {
			'title': pg.title,
			'content': pg.bodytext,
			'last_updated': pg.update_date,
			'page_list': page.objects.all(),
			'plot_div': plot_div2,
			}
	return render(request, 'dashboard/page.html', context)
