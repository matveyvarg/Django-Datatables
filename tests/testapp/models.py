from django.db import models


class RelationClass(models.Model):

	field_1 = models.CharField(max_length=10, null=True)


class TestModel(models.Model):

	char_field = models.CharField(max_length=10)

	text_field = models.TextField()

	int_field = models.IntegerField()

	file_field = models.FileField()

	image_field = models.ImageField()

	uuild_field = models.UUIDField()

	url_field = models.URLField()

	email_field = models.EmailField()

	decimal_field = models.DecimalField(decimal_places=2, max_digits=2)

	float_field = models.FloatField()

	date_time_field = models.DateTimeField()

	boolean_field = models.BooleanField()

	fk_field = models.ForeignKey(RelationClass, on_delete=models.CASCADE, related_name='fk')

	m2m_field = models.ManyToManyField(RelationClass, related_name='m2m')

	o2o_field = models.OneToOneField(RelationClass, on_delete=models.CASCADE, related_name='o2o')