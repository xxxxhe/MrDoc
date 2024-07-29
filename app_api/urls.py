# coding:utf-8
# @文件: urls.py
# @创建者：州的先生
# #日期：2020/3/22
# 博客地址：zmister.com
from django.urls import path,re_path
from app_api import views

urlpatterns = [
    path('manage_token/',views.manage_token,name='manage_token'),# 用户Token管理
    path('get_projects/',views.get_projects,name="api_get_projects"), # 获取文集列表
    path('get_docs/',views.get_docs,name="api_get_docs"), # 获取文集的文档列表
    path('get_level_docs/',views.get_level_docs,name="api_get_level_docs"), # 获取文集的文档列表
    path('get_self_docs/',views.get_self_docs,name="get_self_docs"), # 获取自己的文档列表
    path('get_doc/',views.get_doc,name="api_get_doc"), # 获取单篇文档
    path('get_doc_previous_next/', views.get_doc_previous_next, name="api_get_doc_previous_next"),  # 获取文档上下篇文档
    path('create_project/',views.create_project,name="api_create_project"), # 新建文集
    path('create_doc/',views.create_doc,name="api_create_doc"), # 新建文档
    path('modify_doc/', views.modify_doc, name="api_modify_doc"),  # 修改文档
    path('delete_doc/', views.delete_doc, name="api_delete_doc"),  # 删除文档
    path('upload_img/',views.upload_img,name="api_upload_img"), # 粘贴上传文件
    path('upload_img_url/',views.upload_img_url,name="api_upload_img_url"), # 上传url图片
    path('check_token/',views.check_token,name="api_check_token"), # 验证Token
    # 跳转登录使用
    path('get_timestamp/',views.get_timestamp,name="get_timestamp"), # 获取服务器时间
    path('oauth0/',views.oauth0,name="oauth0"), # Token验证登录，非完整oauth
]
