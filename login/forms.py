from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    # widget = forms.PasswordInput用于指定该字段在form表单里表现为 < input type = 'password' / >，也就是密码输入框。
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
