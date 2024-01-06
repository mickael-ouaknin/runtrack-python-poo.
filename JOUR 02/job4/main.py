class Student:
    def __init__(self, nom, prenom, identifiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__identifiant = identifiant
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, nb_credits):
        if nb_credits > 0:
            self.__credits += nb_credits
            self.__level = self.__studentEval()

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom de l'étudiant :", self.__nom)
        print("Prénom de l'étudiant :", self.__prenom)
        print("Identifiant de l'étudiant :", self.__identifiant)
        print("Nombre de credits de l'étudiant :", self.__credits)
        print("Niveau de l'étudiant :", self.__level)

Jean_Kevin = Student("Doe", "John", 145)

Jean_Kevin.add_credits(10)
Jean_Kevin.add_credits(20)

Jean_Kevin.studentInfo()