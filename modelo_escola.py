
class Professor:
    """Representa um professor no sistema escolar."""

    def __init__(self, nome, disciplina):
        self.nome = nome
        self.disciplina = disciplina

    def lancar_nota(self):
        print(f"Nota lançada com sucesso pelo professor(a) {self.nome} na disciplina {self.disciplina}.")


if __name__ == "__main__":
    prof = Professor("Ana Lima", "Matemática")
    prof.lancar_nota()
    