from django.shortcuts import render

# Create your views here.
# 注册视图
from django.views import View


class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')


# 验证码图片
from django.http.response import HttpResponseBadRequest
from libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from django.http import HttpResponse
class ImageCodeView(View):

    def get(self, request):
        uuid = request.GET.get('uuid')
        # 2.校验数据
        if uuid is None:
            return HttpResponseBadRequest('uuid无效')
        # 3.处理业务
        # 获取图片文本内容和图片二进制代码
        text, image= captcha.generate_captcha()
        # 4.把uuid和图片文本存入redis
        redis_conn = get_redis_connection('default')  # 获取redis客户端
        # 5.写入redis(是字符串)
        # key 设置为uuid
        # seconds过期秒数300秒5分钟过期时间
        # valuetext
        redis_conn.setex('img:%s' % uuid, 300, text)
        # 6.返回响应图片
        return HttpResponse(image, content_type='image/jpeg')
