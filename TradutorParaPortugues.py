from googletrans import Translator

tradutor = Translator()

def traduzir():
    print("\nSEJA BEM VINDO AO SEU TRADUTOR PARA PORTUGUÊS FAVORITO !!!\n")
    traducao_texto = input("Digite o que deseja traduzr: ")
    print("A tradução do seu texto é: ",tradutor.translate(traducao_texto, dest= "pt").text)
    sair()

def sair():
    decisao = input("\nDeseja tradução ?\n"
      "Digite 1 para fazer uma nova tradução\n"
      "digite 2 para sair:" )
    if decisao == "1":
        traduzir()
    elif decisao == "2":
        exit()
    else:
        sair()
traduzir()