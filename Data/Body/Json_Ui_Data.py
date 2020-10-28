import random
import json
import string

from Driver.IdentityCard import IdNumber
name = ['13555555555','13657473031','13615750655','13946755805','13687011854']
namedate = random.choice(name)
account_Order={
    'username':namedate,
    'pwd':'a111111',
    'produce':'测试商品7',
    'name':"Test_name%d" % random.randrange(1, 9999, ),
    'phone':random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)),
    'img':'E://AutomationApiTest//Report//Img//selenium_img.jpg',
    'Verification_Code':'000000',
    'Number':''.join(random.sample(string.ascii_letters + string.digits, 10)),
    'IdNumber':IdNumber.generate_myid(),
    'Address':''.join(random.sample(string.ascii_letters + string.digits, 50))
}



