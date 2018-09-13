import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'website.settings'

if __name__ == '__main__':
    # send_mail(
    #     '来自www.my.com的测试邮件',
    #     '欢迎访问www.my.com，这里是刘江的博客和教程站点，本站专注于Python和Django技术的分享！',
    #     'a_zzzka@163.com',
    #     ['iika@qq.com'],
    # )

    subject, from_email, to = '来自www.KKK.com的测试邮件', 'a_zzzka@163.com', 'iika@qq.com'
    text_content = '欢迎访问www.KKK.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.KKK.com" target=blank>www.KKK.com</a>，这里是刘XX的博客和教程站点，专注于Python和Django技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
