 # 导包
import requests

#给接口地址定义变量名称
url = "http://v.juhe.cn/weather/index"
para = {"cityname":"广州","key":"5636609dbe23a2b00dc3b51edcdd67bd"}

 # 发送请求
r = requests.get(url,params=para)
print(r.status_code)
print(r.json())
res = r.json()
print(res["reason"]+'\n')
print("温度："+res["result"]["sk"]["temp"]+"\n")
print("风向："+res["result"]["sk"]["wind_direction"]+'\n')
print("风力："+res["result"]["sk"]["wind_strength"]+'\n')
print("time："+res["result"]["sk"]["wind_strength"]+'\n')
