from application import create_app

if __name__ == '__main__':
    app = create_app(False)
    
    app.config.from_object('config')
    
    app.run(host="0.0.0.0", port="5000")
