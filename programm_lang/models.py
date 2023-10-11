from django.db import models

class ProgramLang(models.Model):
    ACTUALITY = (
        ('Актуален', 'Актуален'),
        ('50 на 50', '50 на 50'),
        ('Стрем', 'Стрем'),
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    actuality = models.CharField(max_length=100, choices=ACTUALITY, default=ACTUALITY[0], null=True)
    video = models.URLField(null=True)
    created_date_lang = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
