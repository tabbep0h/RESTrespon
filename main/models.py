from django.db import models

POST_CHOICES = (
    ('admin', 'Администратор'),
    ('heisenberg', 'Повар'),
    ('waiter', 'Официант'),
)


class Post(models.Model):
    title = models.CharField(choices=POST_CHOICES, max_length=30)


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dad_name = models.CharField(max_length=255)
    username = models.SlugField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


STATUS_CHOICES = (
    ('added', 'Добавлен'),
    ('in_work', 'В готовке'),
    ('canceled', 'Отменен'),
    ('payed', 'Оплачен'),
)


class Order(models.Model):
    table = models.IntegerField(verbose_name='Номер столика')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
