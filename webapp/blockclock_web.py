from app import app
import logging

if __name__ == '__main__':
    # Disable only Flask's HTTP request logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    
    # Run the app
    app.run(debug=False, host='0.0.0.0', port=5010, use_reloader=True)