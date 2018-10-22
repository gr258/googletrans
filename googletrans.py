import json
import urllib,urllib2


class GoogleTrans():
    def __init__(self):
        self.url = 'http://translate.google.cn/translate_a/single?client=gtx&dt=t&ie=UTF-8&oe=UTF-8&sl=en&tl=zh-CN&'

    def trans(self,input):
        txt = "'%s'" % input
        textmod = { 'q' : txt }
        textmod = urllib.urlencode(textmod)

        request = urllib2.Request(url = '%s%s' % (self.url,textmod))
        request.add_header('User-Agent', 'fake-client')

        response = urllib2.urlopen(request)
        response = response.read()

        ctx = ''
        j = json.loads(response)
        for i in j[0]:
            ctx += i[0]
        return ctx
        
if __name__ == '__main__':
    gt = GoogleTrans()
    s = gt.trans('''Hello world.
    Welcome to coding.net.
    Haha.''');
    print(s)
