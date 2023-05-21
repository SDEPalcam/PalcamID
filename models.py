from django.contrib.auth.models import AbstractBaseUser

class Student(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    student_number = models.CharField(max_length=10)
class StudentCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_physical_card_requested = models.BooleanField(default=False)
    # Aquí puedes agregar más campos según sea necesario.
