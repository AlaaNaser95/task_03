from django.shortcuts import render

def welcome(request):
	return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):
	restaurants=[
				{
				'restaurant_name':'Subway',
				'food_type':'Healthy food',
				},
				{
				'restaurant_name':'Macdonalds',
				'food_type':'Fast food',
				},
				{
				'restaurant_name':'Pizza Hut',
				'food_type':'Pizza',
				},
	]

	context = {
			'my_list': restaurants,
	}
	return render(request, 'list.html', context)


def restaurant_detail(request):
	restaurant={
		
				'restaurant_name':'Subway',
				'food_type':'Healthy food',
	}

	context = {
	'my_object':restaurant,

	}
	return render(request, 'detail.html', context)
