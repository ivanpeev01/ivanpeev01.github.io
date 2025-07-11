import subprocess
import time

def start_flask_server():
    """
    Стартира Flask сървъра (чат) на порт 5000.
    """
    print("Starting Flask server on http://127.0.0.1:5000")
    flask_process = subprocess.Popen(["python", "app.py"])
    return flask_process

def start_http_server():
    """
    Стартира HTTP сървъра (разпознаване на образи) на порт 8000.
    """
    print("Starting HTTP server on http://localhost:8000")
    http_process = subprocess.Popen(["python", "-m", "http.server", "8000"])
    return http_process

if __name__ == "__main__":
    # Стартира Flask сървъра
    flask_process = start_flask_server()
    time.sleep(2)  # Малка пауза (2 секунди), за да се уверим, че сървърът е стартирал

    # Стартира HTTP сървъра
    http_process = start_http_server()

    try:
        # Изчакване на процесите, за да продължат да работят
        flask_process.wait()
        http_process.wait()
    except KeyboardInterrupt:
        # Спиране на сървърите при натискане на Ctrl+C
        print("\nShutting down servers...")
        flask_process.terminate()
        http_process.terminate()
