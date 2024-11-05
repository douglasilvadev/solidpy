from abc import ABC, abstractmethod

class Exame(ABC):
    @abstractmethod
    def verifica_condicoes(self):
        pass

class ExameSangue(Exame):
    def verifica_condicoes(self):
        # condições específicas do exame de sangue
        return True
class ExameRaioX(Exame):
    def verifica_condicoes(self):
        # condições específicas do exame de raio-x
        return True

class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verifica_condicoes():
            print(f"{exame.__class__.__name__} aprovado!")

# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()
aprovador = AprovaExame()

aprovador.aprovar_solicitacao_exame(exame_sangue)
aprovador.aprovar_solicitacao_exame(exame_raio_x)
