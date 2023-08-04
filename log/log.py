from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG
from logging import basicConfig
from logging import critical, error, warning, info, debug
from logging import FileHandler, StreamHandler, Filter

class Filtro(Filter):
    def filter(self, record):
        if 'cartão' in record.msg:
            record.msg = 'Vazou a Senha do Cartão. ATENÇÃO!!'
            return True
        return True

file_handler = FileHandler('logs.log', 'a')
file_handler.setLevel(WARNING)
file_handler.addFilter(Filtro())

stream_handler = StreamHandler()

basicConfig(
    level=DEBUG,
    format='%(levelname)s:-*%(asctime)s:-*%(message)s',
    handlers=[file_handler, stream_handler]
)

critical('Deu Erro cartão')