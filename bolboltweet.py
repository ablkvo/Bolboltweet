import requests

txt1="بیرون ز منزل عشاق مدعی است"
txt2="؟؟؟؟؟؟"
gettxt=requests.get('http://www.bolbolzaban.com/api/deepsher/free/%s-%s'%(txt1, txt2))

jt=gettxt.json()
for i in range(len(jt['output'])):
    print ("%s %s"%(jt['output'][0]['m1'], jt['output'][i]['m2']))





