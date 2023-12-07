import csv
import os


# Classe para representar um artigo de notícia
class Artigo:

  def __init__(self, titulo, categoria, texto, palavras_chave):
    self.titulo = titulo
    self.categoria = categoria
    self.texto = texto
    self.palavras_chave = palavras_chave


# Classe para representar o sistema de gerenciamento de notícias
class SistemaNoticias:

  def __init__(self):
    self.artigos = []
    # Lista para armazenar os artigos de notícia
    
    self.arquivo_csv = "artigos.csv"
    # Nome do arquivo CSV para armazenar os dados
    
    self.carregar_artigos()
    # Função para carregar os artigos do arquivo CSV, se existir

  # Função para carregar os artigos do arquivo CSV
  def carregar_artigos(self):
    try:
      with open(self.arquivo_csv, 'r', newline='', encoding='utf-8') as file:  
        # Corrigido: utf-8
        
        leitor = csv.reader(file, delimiter=';')
        for linha in leitor:
          artigo = Artigo(linha[0], linha[1], linha[2], linha[3].split(','))
          self.artigos.append(artigo)
    except FileNotFoundError:
      pass

  # Função para salvar os artigos no arquivo CSV
  def salvar_artigos(self):
    with open(self.arquivo_csv, 'w', newline='',
              encoding='utf-8') as file:  # Corrigido: utf-8
      escritor = csv.writer(file, delimiter=';')
      for artigo in self.artigos:
        escritor.writerow([artigo.titulo, artigo.categoria, artigo.texto,','.join(artigo.palavras_chave)])

  # Função para cadastrar um novo artigo
  def cadastrar_artigo(self):
    titulo = input("\nDigite o título do artigo: ")
    categoria = input("\nDigite a categoria do artigo: ")
    texto = input("\nDigite o texto do artigo (máximo 400 caracteres): ")
    palavras_chave = input("\nDigite as palavras-chave do artigo separadas por vírgula (mínimo 3): ").split(',')

    novo_artigo = Artigo(titulo, categoria, texto, palavras_chave)
    self.artigos.append(novo_artigo)
    self.salvar_artigos()
    print("\nArtigo cadastrado com sucesso!")

  # Função para pesquisar artigos por categoria
  def pesquisar_artigo(self):
    termo_pesquisa = input("Digite a categoria para pesquisa: ")
    resultados = [
        artigo for artigo in self.artigos
        if termo_pesquisa.lower() == artigo.categoria.lower()
    ]

    return resultados

  # Função para listar os artigos
  def listar_artigos(self, artigos):
    for i, artigo in enumerate(artigos, start=1):
      print(f"{i}. Título: {artigo.titulo}, Categoria: {artigo.categoria}, Texto: {artigo.texto}\n")

  # Função para exibir o menu principal e interagir com o usuário
  def menu(self):
    while True:
      print("\n--- Menu ---")
      print("1. Cadastrar Artigo")
      print("2. Pesquisar Artigo por Categoria")
      print("3. Listar Todos os Artigos")
      print("4. Sair")

      opcao = input("Escolha uma opção: ")

      if opcao == '1':
        self.cadastrar_artigo()
      elif opcao == '2':
        resultados_pesquisa = self.pesquisar_artigo()
        if resultados_pesquisa:
          print("\nResultados da pesquisa:")
          self.listar_artigos(resultados_pesquisa)
        else:
          print("\nNenhum artigo encontrado com a categoria informada.")
      elif opcao == '3':
        os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela
        print("\nTodos os artigos:")
        self.listar_artigos(self.artigos)
      elif opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')  
        # Limpa a tela de novo
        print("\nSaindo do programa. Até mais!")
        break
      else:
        print("\nOpção inválida. Tente novamente.")


# Exemplo de uso
sistema_noticias = SistemaNoticias()
sistema_noticias.menu()
