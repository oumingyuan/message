from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

# 短信应用SDK AppID
app_id = 1400207953  # SDK AppID是1400开头

# 短信应用SDK AppKey
app_key = "dcf8015432958a158b0a40b0c45e6706"

# 需要发送短信的手机号码
phone_numbers = ["13336980260"]

# 短信模板ID，需要在短信应用中申请
template_id = 324429  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请

# 签名
sms_sign = "明明如月"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`

sms_type = 0  # Enum{0: 普通短信, 1: 营销短信}
s_sender = SmsSingleSender(app_id, app_key)
try:
    result = s_sender.send(sms_type, 86, phone_numbers[0],
                           "【腾讯云】您的验证码是: 5678")
    print(result)
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)
