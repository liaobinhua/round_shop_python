from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.


class CommodityCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TPE = (
        (1, "一级类"),
        (2, "二级类"),
        (3, "三级类"),
    )

    name = models.CharField(default="", max_length=60, verbose_name="分类名称",
                            help_text="分类名称")
    code = models.CharField(default="", max_length=30, verbose_name="分类code",
                            help_text="分类code")
    desc = models.TextField(default="", verbose_name="分类描述",
                            help_text="分类描述")
    category_type = models.IntegerField(choices=CATEGORY_TPE,
                                        verbose_name="分类级别",
                                        help_text="分类级别")
    parent_category = models.ForeignKey("self", null=True, blank=True,
                                        on_delete=models.CASCADE,
                                        verbose_name="父类级别",
                                        help_text="父类级别")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航",
                                 help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CommodityCategoryBrand(models.Model):
    """
    品牌名
    """
    category = models.ForeignKey(CommodityCategory, related_name='brands',
                                 on_delete=models.CASCADE,
                                 null=True, blank=True, verbose_name="商品类")
    name = models.CharField(default="", max_length=30, verbose_name="品牌名",
                            help_text="品牌名")
    desc = models.TextField(default="", max_length=200,
                            verbose_name="品牌描述", help_text="品牌描述")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌名"
        verbose_name_plural = verbose_name
        db_table = "commodity_commoditybrand"

    def __str__(self):
        return self.name


class Commodity(models.Model):
    """
    商品
    """
    category = models.ForeignKey(CommodityCategory, on_delete=models.CASCADE,
                                 verbose_name="商品分类")
    commodity_sn = models.CharField(default="", max_length=50,
                                    verbose_name="商品货码")
    name = models.CharField(max_length=100, verbose_name="商品名")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    market_price = models.FloatField(default=0, verbose_name="市场价格")
    shop_price = models.FloatField(default=0, verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
    goods_desc = UEditorField(default='', width=1000, height=300,
                              imagePath='commodity/images',
                              filePath="Commodity/files", verbose_name="内容")
    ship_fee = models.BooleanField(default=True, verbose_name="是否免运费")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True,
                                          blank=True, verbose_name="封面图")
    is_new = models.BooleanField(default=False, verbose_name="是否新品")
    is_hot = models.BooleanField(default=False, verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    category = models.ForeignKey(CommodityCategory, related_name="category",
                                 on_delete=models.CASCADE,
                                 verbose_name="商品类")
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  related_name='commodity')

    class Meta:
        verbose_name = '首页商品类广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.commodity.name


class CommodityImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Commodity, verbose_name="商品",
                              on_delete=models.CASCADE,
                              related_name="image")
    image = models.ImageField(upload_to="", null=True, blank=True,
                              verbose_name="图片")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.commodity.name


class Banner(models.Model):
    """
    轮播的商品
    """
    goods = models.ForeignKey(Commodity, verbose_name="商品",
                              on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
    index = models.IntegerField(default=0, verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = '轮播商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.commodity.name


class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20,
                                verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
