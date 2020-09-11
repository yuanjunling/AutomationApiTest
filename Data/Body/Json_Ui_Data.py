import random

account_Order={
    'username':'13577777777',
    'pwd':'a111111',
    'produce':'姬存希官方正品水光清透隔离防晒乳隔离紫外线面部身体小晶钻新品',
    'name':"Test_name%d" % random.randrange(1, 9999, ),
    'phone':random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)),
    'img':'E://AutomationApiTest//Report//Img//selenium_img.png'
}
print(account_Order['name'])
