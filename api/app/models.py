from django.db import models

class Status(models.TextChoices):
    ATIVO = 'A','Ativo'
    INATIVO = 'I','Inativo'

class Pessoa(models.Model):
    ps_status = models.CharField(max_length=1,choices=Status.choices,default=Status.ATIVO)
    ps_nome = models.CharField(max_length=120)

    class Meta:
        abstract = True

class Dependente(Pessoa):
    ps_idade = models.IntegerField()
    ps_responsavel = models.ForeignKey(Responsavel,on_delete=models.PROTECT,related_name='dependentes')

class Responsavel(Pessoa):
    ps_idade = models.IntegerField()

class Medico(Pessoa):
    ps_crm = models.CharField(max_length==8)

class Medicamento(models.Model):
    md_status = models.CharField(max_length=1,choices=Status.choices,default=Status.ATIVO)
    md_dosagem = models.CharField(max_length=20)
    md_dependente = models.ForeignKey()
    md_quantidade = models.IntegerField()



    #  md_medico = models.ForeignKey(Medico,on_delete=models.CASCADE,related_name='medicamentos')