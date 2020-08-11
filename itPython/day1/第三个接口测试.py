#导入第三方库
import requests

#定义接口地址和参数
url="http://v.juhe.cn/weather/geo"
para={"key":"5636609dbe23a2b00dc3b51edcdd67bd","lon":"113.81","lat":"23.13"}
#发送请求
r=requests.post(url,data=para)
res=r.json()
print(res)