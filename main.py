from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.datetime.now()
    formatted_date_time = now.strftime('%d/%m/%Y %H:%M')

    html_content = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>As Meninas Super Poderosas</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            font-family: 'Roboto', sans-serif;
            background-color: #e2e8f0; /* bg-blue-100 */
            color: #2d3748; /* gray-800 */
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        .header-bg {{
            background: linear-gradient(to right, #4c51bf, #667eea); /* bg-indigo-700 to indigo-500 */
        }}
        .button-primary {{
            background-color: #4c51bf; /* indigo-700 */
            transition: background-color 0.3s ease;
        }}
        .button-primary:hover {{
            background-color: #667eea; /* indigo-500 */
        }}
        .card {{
            background-color: #ffffff;
            border-radius: 0.75rem; /* rounded-xl */
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-xl */
        }}
    </style>
</head>
<body class="flex flex-col min-h-screen">

<header class="header-bg text-white p-4 shadow-lg">
    <div class="container mx-auto flex justify-between items-center">
        <a href="/" class="text-3xl font-bold tracking-tight">As Meninas Super Poderosas</a>
        <nav>
            <ul class="flex space-x-6">
                <li><a href="#" class="text-lg hover:underline">Serviços</a></li>
                <li><a href="#" class="text-lg hover:underline">Sobre</a></li>
                <li><a href="#" class="text-lg hover:underline">Contato</a></li>
            </ul>
        </nav>
    </div>
</header>

<main class="flex-grow container mx-auto px-4 py-12 flex flex-col items-center justify-center">
    <div class="card p-8 md:p-12 text-center max-w-4xl w-full">
        <h1 class="text-5xl md:text-6xl font-extrabold text-gray-800 mb-6 leading-tight">
            As Meninas Super Poderosas: Seu Projeto na Nuvem!
        </h1>
        <p class="text-xl text-gray-600 mb-8">
            Experimente o poder do desenvolvimento web com Flask e um design moderno.
        </p>

        <div class="flex flex-wrap justify-center gap-6 mb-8">
            <div class="w-full sm:w-1/3 p-2 flex flex-col items-center">
                <img src="/static/images/foto1.jpg" alt="Florzinha" class="rounded-lg shadow-md w-48 h-48 object-cover transform transition-transform duration-300 hover:scale-105" onerror="this.onerror=null;this.src='https://placehold.co/192x192/ff9999/ffffff?text=Florzinha';">
                <p class="mt-2 text-lg font-semibold text-pink-600">Florzinha</p>
            </div>
            <div class="w-full sm:w-1/3 p-2 flex flex-col items-center">
                <img src="/static/images/foto3.jpeg" alt="Lindinha" class="rounded-lg shadow-md w-48 h-48 object-cover transform transition-transform duration-300 hover:scale-105" onerror="this.onerror=null;this.src='https://placehold.co/192x192/9999ff/ffffff?text=Lindinha';">
                <p class="mt-2 text-lg font-semibold text-blue-600">Lindinha</p>
            </div>
            <div class="w-full sm:w-1/3 p-2 flex flex-col items-center">
                <img src="/static/images/foto2.jpg" alt="Docinho" class="rounded-lg shadow-md w-48 h-48 object-cover transform transition-transform duration-300 hover:scale-105" onerror="this.onerror=null;this.src='https://placehold.co/192x192/99ff99/ffffff?text=Docinho';">
                <p class="mt-2 text-lg font-semibold text-green-600">Docinho</p>
            </div>
        </div>

        <div class="mt-8 text-lg text-gray-700">
            <p>Data e Hora Atuais: <span class="font-bold text-blue-700">{formatted_date_time}</span></p>
            <p class="mt-2">Desenvolvido por Cibelle, Ana e Sofia em Fatec Taquaritinga</p>
        </div>
    </div>
</main>

<footer class="bg-gray-900 text-gray-400 py-6 text-center text-sm shadow-inner">
    <div class="container mx-auto px-4">
        <p>&copy; 2024 As Meninas Super Poderosas. Todos os direitos reservados.</p>
        <div class="flex justify-center space-x-4 mt-4">
            <a href="#" class="hover:text-white transition duration-300">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/512px-Logo_of_Twitter.svg.png" alt="Twitter Icon" class="h-6 w-6 rounded-full" onerror="this.onerror=null;this.src='https://placehold.co/30x30/cccccc/333333?text=X';">
            </a>
            <a href="#" class="hover:text-white transition duration-300">
                <img src="https://cdn.pixabay.com/photo/2021/06/15/12/51/facebook-6338507_1280.png" alt="Facebook Icon" class="h-6 w-6 rounded-full" onerror="this.onerror=null;this.src='https://placehold.co/30x30/cccccc/333333?text=FB';">
            </a>
            <a href="#" class="hover:text-white transition duration-300">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/768px-Instagram_icon.png" alt="Instagram Icon" class="h-6 w-6 rounded-full" onerror="this.onerror=null;this.src='https://placehold.co/30x30/cccccc/333333?text=IG';">
            </a>
        </div>
    </div>
</footer>

</body>
</html>
"""
    return render_template_string(html_content, current_datetime=formatted_date_time)

if __name__ == '__main__':
    app.run(debug=True)
