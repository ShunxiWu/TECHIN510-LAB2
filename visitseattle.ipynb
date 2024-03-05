import time
import requests
from bs4 import BeautifulSoup

x=[]
for i in range(1, 39): 
    url = f"https://visitseattle.org/events/page/{i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    res.status_code
    res.text
    open("seattleevents.html", "w", encoding="utf-8").write(res.text)
    selector = "div.search-result-preview > div > h3 > a"
    a_eles = soup.select(selector)
    a_eles
    x.extend([a['href'] for a in a_eles])
print(x)

print(len(x))
print(url)

event=[]
for s in x:
    res2 = requests.get(s)
    if res2.status_code == 200:
        soup2 = BeautifulSoup(res2.text, "html.parser")
        res2.text
        # print(s)
        filename = s.replace('/', '_').replace(':', '_').replace('.', '_') + ".html"
        # print(filename)
        open(filename, "w", encoding="utf-8").write(res2.text)
        selector_name=" div.medium-6.columns.event-top > h1"
        selector_date="div.medium-6.columns.event-top > h4 > span:nth-child(1)"
        selector_location=" div.medium-6.columns.event-top > h4 > span:nth-child(2)"
        selector_type=" div.medium-6.columns.event-top > a:nth-child(3)"
        selector_region=" div.medium-6.columns.event-top > a:nth-child(4)"
        name = soup2.select_one(selector_name).text.strip() if soup2.select_one(selector_name) else "N/A"
        date = soup2.select_one(selector_date).text.strip() if soup2.select_one(selector_date) else "N/A"
        location = soup2.select_one(selector_location).text.strip() if soup2.select_one(selector_location) else "N/A"
        type = soup2.select_one(selector_type).string.strip() if soup2.select_one(selector_type) else "N/A"
        region = soup2.select_one(selector_region).text.strip() if soup2.select_one(selector_region) else "N/A"
        event.append([name, date, location, type, region])
        # event.append(type)
print(event)

print(len(event))

import csv

# Your existing code to scrape and extract event information

# Writing to CSV
csv_header = ["Name", "Date", "Location", "Type", "Region"]

with open("events.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    
    # Write header
    csv_writer.writerow(csv_header)
    
    # Write data
    csv_writer.writerows(event)

print("CSV file 'events.csv' has been created.")

# 读取 CSV 文件
with open("events.csv", "r", newline="", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)  # 跳过标题行
    rows = list(csv_reader)

# 新的 CSV 文件头
csv_header = ["Name", "Date", "Location", "Type", "Region", "Weather"]

# 处理每一行数据
for row in rows:
    # 获取地点信息
    location = row[2]
    
    # 在地点后面加上 "Seattle"
    location_seattle = f"{location}, Seattle"
    
    # 查询地点经纬度信息
    base_url = "https://nominatim.openstreetmap.org/search.php"
    query_params = {
        "q": location_seattle,
        "format": "jsonv2"
    }
    res = requests.get(base_url, params=query_params)
    if res.status_code == 200:
        location_info = res.json()
        if location_info:
            latitude = location_info[0]["lat"]
            longitude = location_info[0]["lon"]
        else:
            latitude = "Not found"
            longitude = "Not found"
    else:
        latitude = "Error"
        longitude = "Error"
    
    # 查询天气信息
    if latitude != "Error" and longitude != "Error":
        weather_url = f"https://api.weather.gov/points/{latitude},{longitude}"
        res_weather = requests.get(weather_url)
        if res_weather.status_code == 200:
            weather_data = res_weather.json()
            forecast_url = weather_data["properties"]["forecast"]
            res_forecast = requests.get(forecast_url)
            if res_forecast.status_code == 200:
                forecast_data = res_forecast.json()
                weather = forecast_data["properties"]["periods"][0]["detailedForecast"]
            else:
                weather = "Error fetching weather"
        else:
            weather = "Error fetching weather"
    else:
        weather = "No weather data"
    
    # 将天气信息添加到原始数据中
    row.append(weather)

# 写入新的 CSV 文件
with open("events_with_weather.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    # 写入标题行
    csv_writer.writerow(csv_header)
    # 写入处理后的数据
    csv_writer.writerows(rows)

print("Weather data has been added to the CSV file 'events_with_weather.csv'.")