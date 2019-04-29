import app

def main():
    try:
        app.inject('127.0.0.1', '8080').start()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
