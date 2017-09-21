import requests
from os.path import basename, join

def download_one(url):
    filename = basename(url)
    target = join("./", filename)

    try:
        print("Fazendo o download de %s" % filename)

        with open(target, 'wb+') as f:
            response = requests.get(url, stream=True)
            for chunk in response.iter_content(4096):
                f.write(chunk)

        print("Download pronto")

    except Exception as e:
        print("Erro no download %s" % e)
def main():
    indice_arquivo=130
    while indice_arquivo<=133:
        download_one("http://busca.tjsc.jus.br/revistajc/revistas/"+str(indice_arquivo)+"/"+str(indice_arquivo)+"0000.pdf")
        indice_arquivo+=1

if __name__ == '__main__':
    main()

'''
    Desafios:
'''