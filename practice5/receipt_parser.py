import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

# продукты
products = re.findall(r"\d+\.\n(.+)", text)

# цены товаров
prices = re.findall(r"Стоимость\n([\d\s]+,\d{2})", text)

price_values = []
for p in prices:
    clean = p.replace(" ", "").replace(",", ".")
    price_values.append(float(clean))

# дата
date = re.search(r"\d{2}\.\d{2}\.\d{4}", text)

# время
time = re.search(r"\d{2}:\d{2}:\d{2}", text)

# итог
total = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)

print("Products:")
for p in products:
    print(p)

print("\nPrices:", price_values)

print("\nCalculated total:", sum(price_values))

if date:
    print("\nDate:", date.group())

if time:
    print("Time:", time.group())

if total:
    print("Receipt total:", total.group(1))