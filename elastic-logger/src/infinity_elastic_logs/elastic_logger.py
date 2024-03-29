from datetime import datetime
from .elasticsearch_sender import ElasticSearchSender

class ElasticLogger:
    def __init__(self, service_name) -> None:
        self.service_name = service_name
        self.sender = ElasticSearchSender() 
        
    def debug(self, message):
        self._send_log(message, 'DEBUG')

    def info(self, message):
        self._send_log(message,'INFO')
        
    def warning(self, message):
        self._send_log(message, 'WARNING')

    def error(self, message):
        self._send_log(message, 'ERROR')

    def critical(self, message):
        self._send_log(message, 'CRITICAL')
            
    def _send_log(self, message, level):
        log = self._create_log(message, level)
        self.sender.send_log(log)
        
    def _create_log(self, message,level):
        return {
            'timestamp': f'{datetime.now().isoformat()}',
            'message': message,
            'level': level,
            'service': self.service_name
        }  
    