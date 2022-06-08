'''
    定义索引类
'''

from haystack import indexes
# 导入需要进行检索的模型类
from bookclass.models import tbook

# 指定丢与某个类的某些数据建立索引
# 索引类名格式：模型类名 + Index
class tbookIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段
    # use_template=True：指定根据表中的哪些字段建立索引文件 的说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    press = indexes.CharField(model_attr="press", null=True)
    comment = indexes.IntegerField(model_attr='comment', null=True)
    praise = indexes.IntegerField(model_attr='praise', null=True)
    price = indexes.IntegerField(model_attr='price', null=True)

    def get_model(self):
        """返回建立索引的模型类"""
        return tbook


    def index_queryset(self, using=None):
        """返回要建立索引的数据查询集"""
        return self.get_model().objects.all()









