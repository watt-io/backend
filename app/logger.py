import logging
import sys

def get_logger(name: str) -> logging.Logger:
    """
    Configura e retorna um logger padronizado para a aplicação.
    Motivo: Logs centralizados permitem rastrear erros e acessos de forma profissional,
    facilitando a observabilidade da aplicação quando rodado no Docker.
    """
    # Cria uma instância de logger com o nome do módulo que o chamou
    logger = logging.getLogger(name)
    
    # Define o nível mínimo de mensagens que serão capturadas (INFO, WARNING, ERROR)
    logger.setLevel(logging.INFO)
    
    # Verifica se o logger já possui handlers para evitar logs duplicados
    if not logger.handlers:
        # Direciona a saída dos logs para o console padrão do sistema (stdout)
        handler = logging.StreamHandler(sys.stdout)
        
        # Define o formato do log: Data/Hora - Nome do Logger - Nível - Mensagem
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Adiciona o configurador ao logger principal
        logger.addHandler(handler)
        
    return logger