list_of_cities = "київ,оДеса     Львів.житоМИР,уЖгОрОд.....ХарКІВ       , слАвУтИч".replace(',', ' ').replace('.', ' ').split()

for city in list_of_cities:
    print(f'Я \U00002764  {city.title()}')
