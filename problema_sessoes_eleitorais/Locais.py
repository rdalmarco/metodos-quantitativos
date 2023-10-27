import random as r


class Locais:

    def gera_locais(class_setores, num_locais):
        num_inst_locais = 0
        inst_locais = []
        i = 0
        while (num_inst_locais < num_locais):
           if(i < 24):
            i += 1
            class_setor = class_setores['chave' + str(i + 1)]['valor']
            if (class_setor == 'urb'):
              random = r.random() < 0.35
              if (random == 1):
                inst_locais.append(i + 1)
                num_inst_locais += 1
              else:
               random = r.random() < 0.10
               if (random == 1):
                  inst_locais.append(i + 1)
                  num_inst_locais += 1
            else :
                i = 0
        return inst_locais
