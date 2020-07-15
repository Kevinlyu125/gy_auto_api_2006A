#扣款测试
import random

import allure

from tools.api import request_tool
from tools.api.request_tool import request


@allure.feature("用户模块")
@allure.story("充值提现模块")
@allure.title("扣款接口-账户余额不足")
def test_charge(db):
    with allure.step("第一步,执行sql语句"):
        res = db.select_execute("SELECT account_name FROM t_cst_account WHERE STATUS = 0 AND account_name IS NOT NULL;")
    with allure.step("第二步,从查询结果中随机获取一条，取第一条数据"):
        account_name = random.choice(res)[0]
    with allure.step("第三步,准备请求数据"):
        data='''{
      "accountName":account_name,
      "changeMoney": 100000
    }'''

    with allure.step("第四步,发送请求"):
        r = request.post