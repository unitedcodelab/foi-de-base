class Verifications:
    def create_post(POST):
        if POST["title"] == "":
            return False, "Titulo não pode ser vazio"
        if not POST["title"][0].isalpha():
            return False, "Titulo deve começar com uma letra" 
        if POST["content"] == "":
            return False, "Conteúdo não pode ser vazio"
        
        return True, "Post criado com sucesso"