# FIXME:Skill 1
import time

import pandas as pd

from skilllist import SkillList
from skillzero import SkillZero
def main():
    skill = SkillList()
    while True:
        op = input("choose a skill from 0 to 10 - (qualquer tecla pra sair )")
        try:
            op_cast = int(op)
        except:
            break
        match op_cast:
            case 0:
                s0 = SkillZero()
                infor = s0.info_readme("README.md")
                print(f"O arquivo foi modificado:{infor}")
                print("Aguarde... carregando docstring class")
                time.sleep(7)
                help(SkillZero)
                print("Aguarde... carregando docstring method")
                time.sleep(7)
                help(s0.info_readme)
            case 1:
                skill.skill_one()
            case 2:
                skill.skill_two()
            case 3:
                skill.skill_three()
            case 4:
                print("Carregar dados de um CSV ")
                skill.skill_four()
            case 5:
                print("Uma aula sobre dicionários...")
                skill.skill_five()
            case 6:
                skill.skill_six()
            case 7:
                skill.skill_seven()
            case 8:
                skill.skill_eight()
            case 9:
                dataframe = pd.read_csv("properties.csv")
                skill.skill_nine(dataframe)
            case 10:
                print("Enviando as atividades")
                skill.skill_ten()
            case _:
                print("encerrando...")
                break

if __name__ == "__main__":
    main()
