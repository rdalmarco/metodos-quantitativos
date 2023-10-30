import random as r


class Locais:

    def gera_locais(class_setores, num_locais, cap_atendi_total):
        num_inst_locais = 0
        inst_locais = {}
        i = 0
        class_setores_atual = class_setores.copy()
        while (num_inst_locais < num_locais):
           if(i < len(class_setores_atual)):
                i += 1
                chave = 'chave' + str(i + 1)
                if chave in class_setores_atual:
                 class_setor = class_setores_atual[chave]['tipo']
                 if (class_setor == 'urb'):
                   random = r.random() < 0.35
                   if (random == 1):
                    cap_atendimento_local = (cap_atendi_total/num_locais) * 1.30
                    inst_locais[chave] = {'valor' : cap_atendimento_local}
                    num_inst_locais += 1
                    class_setores_atual.pop(chave)
                   else:
                       random = r.random() < 0.10
                       if (random == 1):
                          cap_atendimento_local = (cap_atendi_total / num_locais) * 0.70
                          inst_locais[chave] = {'valor' : cap_atendimento_local}
                          num_inst_locais += 1
                          class_setores_atual.pop(chave)
           else :
             i = 0
        return inst_locais
