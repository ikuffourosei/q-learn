from django.db import models

class Topics(models.Model):
    """The database table for topics"""
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.name


class Questions(models.Model):
    """The database table for questions"""
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

    def __str__(self) -> str:
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class User(models.Model):
    """The database table for users"""
    name = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return self.name


class Results(models.Model):
    """The database table for Results"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='results')
    score = models.IntegerField()
    time = models.TimeField()
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='results')

    def __str__(self) -> str:
        return f"{self.user} scored {self.score} in {self.time} on {self.topics}"
