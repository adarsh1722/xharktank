from django.db import models

# Create your models here.



class pitche(models.Model):
    pitcherName = models.TextField(blank= True , null= True)
    pitchTitle = models.TextField(blank= True , null= True)
    pitchIdea = models.TextField(blank= True , null= True)
    askAmount = models.FloatField(blank= True , null= True)
    equity = models.FloatField(blank= True , null= True)
    created = models.DateTimeField(auto_now_add=True , blank= True , null= True)

    def __str__(self):
       return self.pitcherName


class offers(models.Model):
    pitche = models.ForeignKey(pitche, on_delete=models.CASCADE)
    investor = models.TextField(blank= True , null= True)
    amount = models.FloatField(blank= True , null= True)
    equity = models.FloatField(blank= True , null= True)
    comment = models.TextField(blank= True , null= True)
    
    def __str__(self):  
        return self.comment

    class Meta:
        ordering = ['amount']