import edmunds

api_key = 'rpftuam8pj4dawg5nauq8vs5'

edmunds_api = edmunds.Edmunds(api_key)
print edmunds_api.get_makes()
