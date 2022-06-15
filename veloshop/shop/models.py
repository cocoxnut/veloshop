from django.db import models


class Banner(models.Model):
    image = models.ImageField(upload_to='static')

    class Meta:
        verbose_name_plural = 'Banners'


class Category(models.Model):
    category = (
        ('Велосипеды', 'Велосипеды'),
        ('Электросамокаты', 'Электросамокаты'),
    )
    select = models.CharField(max_length=15, choices=category, verbose_name='Choose category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.select


class About(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField(max_length=25, verbose_name='First name')
    surname = models.CharField(max_length=25, verbose_name='Last name')
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Registration'
        verbose_name_plural = 'Registration'

    def __str__(self):
        return f'Name: {self.surname} from: {self.email}'


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=25, verbose_name='Types of vehicle')
    description = models.TextField()
    image = models.ImageField(upload_to='static/products/%Y/%m')
    qty = models.IntegerField(default=0)
    price = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class Buyer(models.Model):
    username = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Buyer'
        verbose_name_plural = 'Buyers'

    def __str__(self):
        return self.username


class OrderItem(models.Model):
    user_name = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    item = models.OneToOneField(Products, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    cost = models.IntegerField()

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'

    def __str__(self):
        return f'Order items : {self.item}'

    def save(self, *args, **kwargs):
        self.cost = self.item.price * self.qty
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.OneToOneField(Buyer, on_delete=models.PROTECT)
    order = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    items = models.ManyToManyField(OrderItem, related_name='items')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f'Order : '

    def save(self, *args, **kwargs):
        if self.id:
            self.qty = sum([i.qty for i in self.items.all()])
        super(Cart, self).save(*args, **kwargs)