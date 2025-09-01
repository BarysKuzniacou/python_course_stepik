usa_dollar_exchange_rate = float(input())
rus_rubbles = int(input())
usa_dollars = int(rus_rubbles/usa_dollar_exchange_rate)
text_message = f"Вы можете получить {usa_dollars}$ за {rus_rubbles} рублей по курсу {usa_dollar_exchange_rate}"
print(text_message)