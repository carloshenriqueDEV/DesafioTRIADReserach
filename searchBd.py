import records


#Recebendo a Requisição

# Criando a conexão com o Banco

db = records.Database(mysql://user:password@localhost/dbtest)# passando o adptador do db,o usuário,senha,o host do banco e o nome do bd


# Fazendo uma consulta no banco
"""Após enviar a query o banco retornar a um objeto que representa a tabela com os filtros aplicados na query, esse objeto de retorno é armazenado na variável tablePostosFotos"""

tablePostosFotos = db.query("""SELECT CNPJ,NomeFantasia FROM dbo.Posto
INNER JOIN dbo.Endereco ON  dbo.Posto.Enderecoid = dbo.Endereco.id
WHERE dbo.Endereco.Cidadade = "São Paulo"
INNER JOIN dbo.FotoPosto ON dbo.Posto.UtimaFotoId = dbo.FotoPosto.id
WHERE dbo.FotoPosto.FotoPosto  IS NOT NULL AND  dbo.FotoPlacar IS NOT NULL;""")


#Convertendo tablePostosFotos para Json
"""A conversão é bem simples com python o objeto tablePostosFotos possui um método export() que recebe com paramentro
o tipo de conversão e retorna um novo objeto convertido, alguns tipos de parâmetros são csv,json,html. """

tablePostosFotosJson = tablePostoFotos.export('json')

#Enviando a resposta ao cliente

