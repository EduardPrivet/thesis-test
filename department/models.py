from django.db import models


class Employee(models.Model):
    first_name = models.CharField(u"имя", max_length=100, db_index=True)
    last_name = models.CharField(u"фамилия", max_length=100)
    middle_name = models.CharField(u"отчество", max_length=100, blank=True, null=True)
    photo = models.ImageField(u"фотография", upload_to="employee/", blank=True, null=True)
    position = models.CharField(u'должность', max_length=100)
    age = models.PositiveIntegerField(u'возраст', blank=True, null=True)
    salary = models.PositiveIntegerField(u'оклад', blank=True, null=True)
    department = models.ForeignKey('Department', verbose_name=u'департамент',
                                   on_delete=models.SET_NULL, related_name='employees',
                                   blank=True, null=True)

    def get_full_name(self):
        return ' '.join([x for x in (self.last_name, self.first_name, self.middle_name) if x])

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = u"сотрудник"
        verbose_name_plural = u"сотрудники"


class Department(models.Model):
    title = models.CharField(u"название", max_length=250)
    director = models.OneToOneField('Employee', on_delete=models.SET_NULL,
                                    verbose_name=u'директор',
                                    related_name='managed_department',
                                    blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u"департамент"
        verbose_name_plural = u"департаменты"


