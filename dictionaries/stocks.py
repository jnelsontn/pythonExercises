stockDict = dict() # dictionary - like a javascript object
stockDict = { 
	'MO':'Altria',
	'PM':'Philip Morris',
	'GM':'General Motors',
	'VTI':'Vanguard Total Stock Market Index' }

purchases = tuple() # tuple or list() like a javascript array
purchases = [
			('MO', 100, '6-April-2017', 70),
			('PM', 100, '6-April-2017', 110),
			('GM', 100, '6-April-2017', 35),
			('VTI', 100, '6-April-2017', 120),
			('MO', 50, '10-April-2017', 75)
			]

portfolio = dict()
for purchase in purchases:
	ticker = purchase[0]
	full_company_name = stockDict[ticker]

	number_of_shares = purchase[1]
	stock_price = purchase[3]
	full_purchase_price = number_of_shares * stock_price

	try:
		portfolio[ticker].append(purchase)
	except KeyError:
		portfolio[ticker] = list()
		portfolio[ticker].append(purchase)

	print("I purchased {} stock for ${}".format(full_company_name, full_purchase_price))

for ticker, purchases in portfolio.items():
	print("---------- {} --------".format(ticker))
	total_portfolio_stock_value = 0
	for purchase in purchases:
		total_portfolio_stock_value += purchase[1] * purchase[3]
		print(purchase)
	print("Total Value of Stock in Portfolio: ${}\n\n".format(total_portfolio_stock_value))



