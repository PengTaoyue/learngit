#导入第三方库
import requests

#定义接口地址和参数
url="http://v.juhe.cn/weather/uni"
# para={"key":"5636609dbe23a2b00dc3b51edcdd67bd"}
para={"key":"5636609dbe23a2b00dc3b51edcdd67b"}

#发送请求
r=requests.get(url,params=para)
res=r.json()
# print(r.json())
print(res["error_code"])