

#创建产品


from tools.api import request_tool

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 3 数字 NHK "
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '创建产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "NHK",
  "colors": [
    "blue","red"
  ],
  "price": 200000,
  "productCode": "${productCode}",
  "productName": "霓虹NHK",
  "sizes": [
    "well","bad"
  ],
  "type": "TV"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)



# 根据产品编码查询产品
def test_getSkuByProdCode(pub_data):
    pub_data["prodCode"] = "${productCode}"
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '根据产品编码查产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]
               }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${prodCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)





# 下架产品
def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '下架产品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)



# 查询产品状态
def test_3(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '查询产品状态'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU/1/3"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]
               }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'endTime': '2018-10-19 10:41:18', 'startTime': '2018-10-18 09:41:18', 'status': '2'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)



# 改产品状态为预售
def test_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '该产品状态为预售'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)




# 修改产品价格
def test_changePriceByProdCode(pub_data):
    pub_data["prodCode"] = "${productCode}"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '修改产品价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '20000', 'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)




# 根据产品编码查询商品
def test_getSkuByProdCode(pub_data):
    pub_data["prodCode"] = "${productCode}"
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '根据产品编码查询商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)




# 修改商品价格
def test_changePrice(pub_data):

    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'SKU':'${skuCode}', 'price': '2000000'}
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)



#查询单个商品
def test_getSKU(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NzE1NTAzMjAyLCJ1c2VySWQiOjEwNDczLCJ1c2VyTmFtZSI6InFnaDcxNCJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'SKU': '${skuCode}'}
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)




#全量增加商品
def test_fullSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/fullSku"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NzE1NTAzMjAyLCJ1c2VySWQiOjEwNDczLCJ1c2VyTmFtZSI6InFnaDcxNCJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '200', 'skuCode': '${skuCode}'}
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)




# 增量调整库存
def test_incrementSku(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/incrementSku"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NzE1NTAzMjAyLCJ1c2VySWQiOjEwNDczLCJ1c2VyTmFtZSI6InFnaDcxNCJ9', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]
               }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'qty': '1', 'skuCode': '${skuCode}'}
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)




# 查询单个商品库存
def test_getSkuRepertory(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuRepertory"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'token': 'eyJ0aW1lT3V0IjoxNTk0NzE1NTAzMjAyLCJ1c2VySWQiOjEwNDczLCJ1c2VyTmFtZSI6InFnaDcxNCJ9', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9'
        , "token": pub_data["token"]
               }
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'skuCode': '${skuCode}'}
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)



#下载某个产品的库存信息
def test_get_file(pub_data):
    file_name = "e:\\sku.xlsx" # 下载文件地址
    pub_data["prodCode"] = "${productCode}"
    method = "GET"  #请求方法，全部大写
    feature = "库存模块"  # allure报告中一级分类
    story = '下载库存信息'  # allure报告中二级分类
    title = "下载库存信息_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/downProdRepertory"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"pridCode":'${productCode}'}
    headers={"token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
    with open(file_name,"rb") as f :
        f.write(r.content)