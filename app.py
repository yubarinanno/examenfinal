from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_geek():
  profile_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Perfil de Programador</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <div class="row justify-content-center mt-5">
                <div class="col-md-6">
                    <div class="card">
                        <img src="https://okawariplease.files.wordpress.com/2017/09/pompompurin.png?w=676" alt="Imagen de perfil">
                        <div class="card-body">
                            <h5 class="card-title">Mical Andrea Roque Huaynate</h5>
                            <p class="card-text">Soy un programadora</p>
                        </div>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item">Lenguajes de Programación: Python, JavaScript, HTML, CSS</li>
                            
                      
                        </ul>
                        <div class="card-body">
                            <a href="#" class="card-link">Contactar</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
  return profile_html


if __name__ == "__main__":
  app.run(debug=True)

