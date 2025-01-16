import csv

input_filename = "country_info.txt"

countries = {}
# with open(input_filename) as country_file:
#     country_file.readline()
#     for row in country_file:
#         data = row.strip("\n").split("|")
#         country, capital, code, code3, dialing, timezone, currency = data
#         country_dict = {
#             "name": country,
#             "capital": capital,
#             "country_code": code,
#             "cc3": code3,
#             "dialing_code": dialing,
#             "timezone": timezone,
#             "currency": currency,
#         }
#         countries[country.casefold()] = country_dict
#
# query = input()
# # print(f"{query}::::{countries[query.casefold()]['capital']}")
# # print(countries)
# not_found = True
# for i in countries:
#     if countries[i]["country_code"].casefold() == query.casefold():
#         print(countries[i]["capital"])
#         not_found = False
#         break
# if not_found:
#     print("Not Available in Dict.")

with open(input_filename, encoding="utf-8", newline="") as file:
    row = csv.DictReader(file, delimiter="|")
    for i in row:
        countries[i["Country"].casefold()] = i
        countries[i["CC"].casefold()] = i

for i, j in countries.items():
    print(i, j)
