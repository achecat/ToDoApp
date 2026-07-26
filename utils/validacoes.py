from datetime import datetime

class ValidadorTarefa:
    def validar_tarefa(titulo, descricao=None, data_str=None):
        '''
        Valida os campos da tarefa.
        Retorna True e none se tudo passar, ou False e uma mensagem de erro
        '''

        #Valida se título esta vazio ou apenas espaços
        if not titulo or not titulo.strip():
            return False, "O título da tarefa não pode estar vazio."

        #Valida tamanho do título
        if len(titulo.strip()) > 100:
            return False, "O título deve conter no máximo 100 caracteres."

        #Valida formato de data
        if data_str:
            try:
                data_obj = datetime.strftime(data_str, "%Y-%m-%d").date()
                if data_obj < datetime.now().date():
                    return False, "A data da tarefa não pode ser no passado."

            except ValueError:
                return False, "Formato de data inválido. Use AAAA-MM-DD"

        return True, None