from django.db import models
# All enums used in the project should be in here


class UFChoices(models.TextChoices):
    AC = "AC", "Acre",
    AL = "AL", "Alagoas",
    AP = "AP", "Amapá",
    AM = "AM", "Amazonas",
    BA = "BA", "Bahia",
    CE = "CE", "Ceará",
    DF = "DF", "Distrito Federal",
    ES = "ES", "Espírito Santo",
    GO = "GO", "Goiás",
    MA = "MA", "Maranhão",
    MS = "MS", "Mato Grosso do Sul",
    MT = "MT", "Mato Grosso",
    MG = "MG", "Minas Gerais",
    PA = "PA", "Pará",
    PB = "PB", "Paraíba",
    PR = "PR", "Paraná",
    PE = "PE", "Pernambuco",
    PI = "PI", "Piauí",
    RJ = "RJ", "Rio de Janeiro",
    RN = "RN", "Rio Grande do Norte",
    RS = "RS", "Rio Grande do Sul",
    RO = "RO", "Rondônia",
    RR = "RR", "Roraima",
    SC = "SC", "Santa Catarina",
    SP = "SP", "São Paulo",
    SE = "SE", "Sergipe",
    TO = "TO", "Tocantins"
