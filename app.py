from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Proyecto Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
                background-color: #f0f2f5;
            }
            h1 {
                color: #2c3e50;
                font-size: 2.5em;
            }
            h2 {
                color: #e67e22;
                font-weight: normal;
            }
            .container {
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <!-- TÍTULO -->
            <h1>hola estrellitas </h1>
            
            <!-- SUBTÍTULO -->
            <h2>Prueba de Daniela Alexandra Cárdenas Maldonado</h2>
        </div>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)