from people.models import Student

class Verifications:
    def create_post(POST):
        if POST["title"] == "":
            return False, "Titulo não pode ser vazio"
        if not POST["title"][0].isalpha():
            return False, "Titulo deve começar com uma letra" 
        if POST["content"] == "":
            return False, "Conteúdo não pode ser vazio"
        
        if Student.objects.filter(nick=POST["title"]).exists():
            return False, "Um post não pode ter o mesmo nome que um estudante"
        
        return True, "Post criado com sucesso"
    

    def get_post(post, student_nick):
        if post.author.nick != None and post.author.nick != student_nick:
            return False, "Post não pertence ao estudante"
        return True, "Post encontrado"