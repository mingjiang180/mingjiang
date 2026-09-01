#!/usr/bin/env python3
import urllib.request
import json
from datetime import datetime


def get_weather(city="Beijing"):
    """获取指定城市的天气信息"""
    url = f"https://wttr.in/{city}?format=j1"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode())
            current = data["current_condition"][0]
            return {
                "city": city,
                "temp_c": current["temp_C"],
                "humidity": current["humidity"],
                "description": current["weatherDesc"][0]["value"],
                "wind_speed": current["windspeedKmph"],
            }
    except Exception as e:
        return {"error": str(e)}


def main():
    """主函数：显示今天的天气情况"""
    print("=" * 40)
    print(f"今日天气查询 - {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 40)

    weather = get_weather("Beijing")

    if "error" in weather:
        print(f"获取天气失败: {weather['error']}")
    else:
        print(f"城市: {weather['city']}")
        print(f"温度: {weather['temp_c']}°C")
        print(f"湿度: {weather['humidity']}%")
        print(f"天气: {weather['description']}")
        print(f"风速: {weather['wind_speed']} km/h")

    print("=" * 40)


if __name__ == "__main__":
    main()
