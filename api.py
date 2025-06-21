#api = application programming interface
#como fazer 2 sistemas conversarem entre si?
#interface = porta de entrada, forma de estabelecer comunicação

#cliente = alguém que está utilizando pc, tablet, sistema, etc
#no meio, uma API
#atrás, um API Server
#o cliente envia um request pra API, que vai passar essa requisição pro servidor
#depois disso, o servidor vai responder pra API e então responder pro cliente

#exemplo banco:
#cliente solicita saber seu saldo pra API, a API pergunta pro servidor, e então o servidor retorna pra API e a API entrega pro cliente

#API REST - Representational State Transfer
#estilo de arquitetura pra desenvolvimento de APIs
#conjunto de regras que permita que a comunicação seja fluida
#baseado no protocolo HTTP

"""
get
post
put
delete
patch
"""

#recurso = endpoint
#formato de representação
#devolve em JSON ou XML

#API Rest x API Restful
#Restful: quando respeita todos os padrões do REST