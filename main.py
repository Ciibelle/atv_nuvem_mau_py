# Importa as classes necessárias do Flask
from flask import Flask, render_template_string # Usaremos render_template_string
import datetime # Módulo para trabalhar com datas e horas

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota para a página inicial ('/')
@app.route('/')
def home():
    # Obtém a data e hora atual
    now = datetime.datetime.now()
    # Formata a data e hora no mesmo formato do exemplo PHP
    formatted_date_time = now.strftime('%d/%m/%Y %H:%M')

    # HTML completo como uma string Python multi-linha
    # Usamos f-string para injetar a data/hora diretamente
    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PROJETO_NUVEM - Flask Simples</title>

    <!-- Importa Bootstrap -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" xintegrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

</head>
<body>

<header>
    <div class="px-3 py-2 text-bg-dark border-bottom">
      <div class="container">
        <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
          <a href="/" class="d-flex align-items-center my-2 my-lg-0 me-lg-auto text-white text-decoration-none">
            <!-- Imagem do logotipo Fatec -->
            <img src="https://www.fatecclub.gregmaster.com.br/wp-content/uploads/2018/09/logo-fatec.png" width="120px" height="50px" alt="logotipo Fatec">
          </a>
          <ul class="nav col-12 col-lg-auto my-2 justify-content-center my-md-0 text-small">
            <li>
              <a href="#" class="nav-link text-white">Home</a>
            </li>
            <li>
              <a href="#" class="nav-link text-white">Dashboard</a>
            </li>
            <li>
              <a href="#" class="nav-link text-white">Pedidos</a>
            </li>
            <li>
              <a href="#" class="nav-link text-white">Produtos</a>
            </li>
            <li>
              <a href="#" class="nav-link text-white">Clientes</a>
            </li>
            <li>
              <a href="#" class="nav-link text-white">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
</header>


<div class="container">
  <div class="row pt-3">
    <div class="col-sm">
        <h1 class="mt-5">Hospedado !!!</h1>
        <p class="lead">
            Este é um exemplo simples usando **Flask** e Bootstrap. <br>
        </p>
        <br>
        <p>
            <b>Data e Hora:</b>
            <!-- A data e hora formatada é injetada aqui -->
            {formatted_date_time}
        </p>
        <p><b>Unidade:</b> Fatec Taquaritinga</p>
        <p><b>Prof.:</b> Mauricio de Oliveira Dian</p>
    </div>
    <div class="col-sm">
        <!-- Imagem relacionada ao PHP (mantida para contexto visual) -->
        <img src="https://www.site.pt/wp-content/uploads/2022/01/o-que-e-php.jpg" alt="php-imagem" width="600px" height="370px">
    </div>
  </div>
</div>


<div class="container">
  <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
    <div class="col-md-4 d-flex align-items-center">
      <a href="/" class="mb-3 me-2 mb-md-0 text-body-secondary text-decoration-none lh-1">
        <!-- Imagem do logotipo Bootstrap -->
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSff90_MR_zyln7GdER-nrk-YCbgDLc3Lu2BQ&s" alt="bootstrap-logotipo" width="40px" height="30px">
      </a>
      <span class="mb-3 mb-md-0 text-body-secondary">Criado com Bootstrap © 2024 Company, Inc</span>
    </div>

    <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
      <li class="ms-3">
        <a class="text-body-secondary" href="#">
            <!-- Ícone do Twitter -->
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/512px-Logo_of_Twitter.svg.png?20220821125553" alt="twitter" width="30px" height="30px">
        </a>
      </li>
      <li class="ms-3">
        <a class="text-body-secondary" href="#">
            <!-- Ícone do Facebook -->
            <img src="https://cdn.pixabay.com/photo/2021/06/15/12/51/facebook-6338507_1280.png" alt="facebook" width="30px" height="30px">
        </a>
      </li>
      <li class="ms-3">
        <a class="text-body-secondary" href="#">
            <!-- Ícone do Instagram -->
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png" alt="instagram" width="30px" height="30px">
        </a>
      </li>
    </ul>
  </footer>
</div>

</body>
</html>
"""
    # Retorna o HTML renderizado diretamente
    return render_template_string(html_content, current_datetime=formatted_date_time)

# Garante que o servidor Flask seja executado apenas quando o script for executado diretamente
if __name__ == '__main__':
    # Roda a aplicação em modo debug (útil para desenvolvimento, recarrega automaticamente)
    app.run(debug=True)
