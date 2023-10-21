'''
Rishu has to buy 1000 mangoes and cost of each mango is 20 Rs. But Rishu has only 10 Rs. He wants to buy 5 mangoes.
How much money should Rishu need more to buy 5 mangoes?

Author: Rishu Gupta
Date: 21/10/2023
'''

cost_per_unit_mango = 20
money_rishu_has = 10
mango_rishu_wants = 5
money_rishu_needed = mango_rishu_wants * cost_per_unit_mango - money_rishu_has
print("Money Rishu Needed to Buy 5 Mangoes: ",money_rishu_needed,"Rs.")
