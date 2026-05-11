# =============================================================
# SISTEMA DE ALUGUEL DE BICICLETAS - Análise de Abstração
# =============================================================
#
# ATRIBUTOS ESSENCIAIS (relevantes para o controle do sistema):
#   1. id_bicicleta    - identifica unicamente cada bicicleta no sistema
#   2. status          - indica se a bicicleta está disponível ou alugada
#   3. cpf_cliente     - identifica o cliente responsável pelo aluguel
#   4. data_hora_retirada - registra quando o aluguel foi iniciado (para calcular cobrança)
#
# ATRIBUTOS IRRELEVANTES (detalhes descartáveis para o sistema):
#   1. cor             - a cor da bicicleta não afeta a lógica de aluguel ou cobrança
#   2. marca           - a fabricante não interfere no controle operacional do sistema
# =============================================================
