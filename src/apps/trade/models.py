from django.db import models
from datetime import datetime
from commodity.models import Commodity
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="用户")
    goods = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                              verbose_name="商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)" . format(self.commodity.name, self.nums)


class OrderInfo(models.Model):
    """
    订单
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("PAYING", "支付中"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name="用户")
    order_sn = models.CharField(max_length=30, null=True, blank=True,
                                verbose_name="订单号")
    trade_no = models.CharField(max_length=100, unique=True, null=True,
                                verbose_name="交易号")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying",
                                  max_length=30, verbose_name="订单状态")
    post_script = models.CharField(max_length=200, verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True, blank=True,
                                    verbose_name="支付时间")
    # user info
    address = models.CharField(default="", max_length=100,
                               verbose_name="收获地址")
    signer_name = models.CharField(default="", max_length=20,
                                   verbose_name="签收人")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "商品订单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)


class OrderGoods(models.Model):
    """
    订单的商品详情
    """
    order = models.ForeignKey(OrderInfo, verbose_name="订单信息",
                              related_name="goods", on_delete=models.CASCADE)
    goods = models.ForeignKey(Commodity, verbose_name="商品",
                              on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name="添加时间")

    class Meta:
        verbose_name = "订单的商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
