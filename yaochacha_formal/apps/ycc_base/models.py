#coding=utf-8
from django.db import models


class TDrugVisitRecord(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    drug_id = models.IntegerField(db_column='drug_id', blank=True, null=True)  # 药品ID
    drug_name = models.CharField(db_column='drug_name', max_length=100, blank=True)  # 药品名称
    manufacturer = models.CharField(db_column='manufacturer', max_length=100, blank=True)  # 生产厂家
    # 访问类型：bar_code-条形码，supervision_code-电子监管码，other-其他，dialogue-小程序对话，history-历史记录
    visit_type = models.CharField(db_column='visit_type', max_length=100, blank=True)
    visit_ip = models.CharField(db_column='visit_ip', max_length=100, blank=True)  # 访问者IP地址
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间
    open_id = models.CharField(db_column='open_id', max_length=100, blank=True)  # 微信号
    user_id = models.IntegerField(db_column='user_id', blank=True, null=True)  # 用户ID（对应y_user_info表）
    unique_key = models.CharField(db_column='unique_key', max_length=256, blank=True)  # 唯一标识

    class Meta:
        managed = False
        db_table = 't_bg_drug_visit_record'


class TCompanyVisitRecord(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    pc_name = models.CharField(db_column='pc_name', max_length=100, blank=True)  # 企业名称
    pc_type = models.IntegerField(db_column='pc_type', blank=True, null=True)  # 企业类别：1-生产企业，2-经营企业，3-非药企
    visit_type = models.CharField(db_column='visit_type', max_length=100, blank=True)  # 访问类型
    visit_ip = models.CharField(db_column='visit_ip', max_length=100, blank=True)  # 访问者IP地址
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间
    open_id = models.CharField(db_column='open_id', max_length=100, blank=True)  # 微信号
    user_id = models.IntegerField(db_column='user_id', blank=True, null=True)  # 用户ID（对应y_user_info表）
    unique_key = models.CharField(db_column='unique_key', max_length=256, blank=True)  # 唯一标识

    class Meta:
        managed = False
        db_table = 't_bg_company_visit_record'


class TDataVisitRecord(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    drug_id = models.IntegerField(db_column='drug_id', blank=True, null=True)  # 药品ID
    visit_type = models.CharField(db_column='visit_type', max_length=100, blank=True)  # 访问类型：1-扫描条形码，
    # 2-扫描电子监管码，3-首页大搜索，4-热门搜索，5-找药品菜单，6-查企业菜单，7-地址电话菜单，8-附件的药店菜单，
    # 9-健康头条，10-最新评论，11-药品说明书，12-生产企业，13-药品成分，14-饮食禁忌，15-药品价格，16-临床病症，
    # 17-临床资料/疗效分析，18-药物相互作用，19-不良反应，20-药理毒理，21-药品资讯，22-质量不合格公告，23-相关厂家 ，
    # 24-同类药品，25-药监信息，26-全国药店，27-更多评论
    visit_ip = models.CharField(db_column='visit_ip', max_length=100, blank=True)  # 访问者IP地址
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间
    open_id = models.CharField(db_column='open_id', max_length=100, blank=True)  # 微信号
    user_id = models.IntegerField(db_column='user_id', blank=True, null=True)  # 用户ID（对应y_user_info表）
    unique_key = models.CharField(db_column='unique_key', max_length=256, blank=True)  # 唯一标识

    class Meta:
        managed = False
        db_table = 't_bg_data_visit_record'


class TDrugStatistics(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    drug_id = models.IntegerField(db_column='drug_id', blank=True, null=True)  # 药品ID
    drug_name = models.CharField(db_column='drug_name', max_length=100, blank=True)  # 药品名称
    manufacturer = models.CharField(db_column='manufacturer', max_length=100, blank=True)  # 生产厂家
    bar_code = models.IntegerField(db_column='bar_code', blank=True, null=True)  # 扫码
    supervision_code = models.IntegerField(db_column='supervision_code', blank=True, null=True)  # 电子监管码
    other = models.IntegerField(db_column='other', blank=True, null=True)  # 其他
    path = models.IntegerField(db_column='path', blank=True, null=True)  # 链接
    history = models.IntegerField(db_column='history', blank=True, null=True)  # 历史记录
    view_count = models.IntegerField(db_column='view_count', blank=True, null=True)  # 浏览量
    attention_count = models.IntegerField(db_column='attention_count', blank=True, null=True)  # 关注量
    comment_count = models.IntegerField(db_column='comment_count', blank=True, null=True)  # 评论量
    update_date = models.DateTimeField(db_column='update_date', blank=True, null=True)  # 更新时间
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间

    class Meta:
        managed = False
        db_table = 't_bg_drug_statistics'


class TCompanyStatistics(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    pc_name = models.CharField(db_column='pc_name', max_length=100, blank=True)  # 药品名称
    pc_type = models.IntegerField(db_column='pc_type', blank=True, null=True)  # 扫码
    drug_relation = models.IntegerField(db_column='drug_relation', blank=True, null=True)  # 电子监管码
    path = models.IntegerField(db_column='path', blank=True, null=True)  # 链接
    history = models.IntegerField(db_column='history', blank=True, null=True)  # 历史记录
    view_count = models.IntegerField(db_column='view_count', blank=True, null=True)  # 浏览量
    attention_count = models.IntegerField(db_column='attention_count', blank=True, null=True)  # 关注量
    comment_count = models.IntegerField(db_column='comment_count', blank=True, null=True)  # 评论量
    update_date = models.DateTimeField(db_column='update_date', blank=True, null=True)  # 更新时间
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间

    class Meta:
        managed = False
        db_table = 't_bg_company_statistics'


class TDataStatistics(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    statistics_type = models.IntegerField(db_column='statistics_type', blank=True, null=True)  # 统计类型：1-扫描条形码
    # ，2-扫描电子监管码，3-首页大搜索，4-热门搜索，5-找药品菜单，6-查企业菜单，7-地址电话菜单，8-附件的药店菜单，
    # 9-健康头条，10-最新评论，11-药品说明书，12-生产企业，13-药品成分，14-饮食禁忌，15-药品价格，16-临床病症，
    # 17-临床资料/疗效分析，18-药物相互作用，19-不良反应，20-药理毒理，21-药品资讯，22-质量不合格公告，23-相关厂家 ，
    # 24-同类药品，25-药监信息，26-全国药店，27-更多评论
    statistics_count = models.IntegerField(db_column='statistics_count', blank=True, null=True)  # 统计数量
    add_date = models.DateTimeField(db_column='add_date', blank=True, null=True)  # 添加时间

    class Meta:
        managed = False
        db_table = 't_bg_data_statistics'


class TLastRecord(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    liulan = models.IntegerField(db_column='liulan', blank=True, null=True)  # 浏览量最大ID
    guanzhu = models.DateTimeField(db_column='guanzhu', blank=True, null=True)  # 关注的最后时间
    pinglun = models.IntegerField(db_column='pinglun', blank=True, null=True)  # 评论的最大ID
    company = models.IntegerField(db_column='company', blank=True, null=True)  # 企业访问记录表最大ID
    drug = models.IntegerField(db_column='drug', blank=True, null=True)  # 药品访问记录表最大ID
    max_drug_id = models.IntegerField(db_column='max_drug_id', blank=True, null=True)  # 药品最大ID
    max_company_id = models.IntegerField(db_column='max_company_id', blank=True, null=True)  # 企业最大ID

    class Meta:
        managed = False
        db_table = 't_bg_last_record'


class TDrugInfo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    drug_id = models.IntegerField(db_column='drugID', blank=True, null=True)  # 药品ID
    drug_name = models.CharField(db_column='namecn', max_length=100, blank=True)  # 药品名称
    refdrugcompanyname = models.CharField(db_column='refdrugcompanyname', max_length=100, blank=True)  # 生产厂家

    class Meta:
        managed = False
        app_label = 'app01'
        db_table = 't_drugInfo'


class YGuanZhu(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    type = models.IntegerField(db_column='type', blank=True, null=True)  # 用户关注类别，0为关注的药品 ，1 为关注的药企
    subject_id = models.CharField(db_column='subject_id', max_length=100, blank=True)  # 用户关注主体的id
    state = models.IntegerField(db_column='state', blank=True, null=True)  # 关注状态 1为关注 ， 0为取消关注

    class Meta:
        managed = False
        app_label = 'app02'
        db_table = 'y_guanzhu'


class YLiuLan(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    object_type = models.IntegerField(db_column='object_type', blank=True, null=True)  # 浏览主体类别 ， 0为药品 ， 1为药企
    object_id = models.CharField(db_column='object_id', max_length=100, blank=True)  # 浏览主体的id

    class Meta:
        managed = False
        app_label = 'app02'
        db_table = 'y_liulan'


class YPingLun(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    object_type = models.IntegerField(db_column='object_type', blank=True, null=True)  # 评论主体类别 ， 0为药品， 1为药企 ， 2为新闻
    object_id = models.CharField(db_column='object_id', max_length=100, blank=True)  # 评论主体id

    class Meta:
        managed = False
        app_label = 'app02'
        db_table = 'y_pinglun'


class YUserInfo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # ID
    open_id = models.IntegerField(db_column='openid', blank=True, null=True)  # 微信号
    user_session = models.CharField(db_column='user_session', max_length=100, blank=True)  # 应用端登录凭证

    class Meta:
        managed = False
        app_label = 'app02'
        db_table = 'y_user_info'
