from django import forms
# from django.contrib.auth import get_user_model
#
# User = get_user_model()

# 用户注册表单
class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=15, error_messages={
        'required': '请输入账号!',
        'min_length': '账号至少输入4位!',
        'max_length': '账号长度不能超过15位！'
    })
    # 邮箱
    email = forms.EmailField(required=False)
    # 密码
    password = forms.CharField(required=True, min_length=6, max_length=15, error_messages={
        'required': '请填写密码！',
        'min_length': '密码至少输入6位数!',
        'max_length': '密码长度不能超过15位！'
    })
    # # 学院
    college = forms.CharField(required=False)

# 用户登录表单
class UserLoginForm(forms.Form):
    # 登录的 username = forms.CharField 需要和注册中的username = forms.CharField 的 CharField相匹配
    username = forms.CharField(required=True, min_length=4, max_length=15, error_messages={
        'required': '请输入账号!',
        'min_length': '账号至少输入4位!',
        'max_length': '账号长度不能超过15位！'
    })
    # 密码
    password = forms.CharField(required=True, min_length=6, max_length=15, error_messages={
        'required': '请填写密码！',
        'min_length': '密码至少输入6位数!',
        'max_length': '密码长度不能超过15位！'
    })

# 用户修改密码表单
class ChangepwdForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=15, error_messages={
        'required': '请输入账号!',
        'min_length': '账号至少输入4位!',
        'max_length': '账号长度不能超过15位！'
    })

    # old_password = forms.CharField(label='原始密码', widget=forms.PasswordInput())
    new_pwd = forms.CharField(label='新密码', widget=forms.PasswordInput())
    new_pwds = forms.CharField(label='确认新密码', widget=forms.PasswordInput())