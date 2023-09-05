from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)   # null=True는 데이터베이스에서 null 허용, blank=True는 form.is_valid()에서 입력데이터 검증시 값이 없어도 된다는 의미
    voter = models.ManyToManyField(User, related_name='voter_question')    # 추천인 추가

    def __str__(self):  # Question.objects.all() 할때 id값 대신 subject값 표시
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')