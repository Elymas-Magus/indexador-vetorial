# indexador-vetorial

Esta aplicação é capaz de receber uma ou mais consultas, inseridas via arquivo xml (queries.txt), e então ela procura na base de dados, usando o modelo vetorial de busca e indexação, os arquivos que mais se assemelham as buscas.

Para tal feito o modelo vetorial atribui pesos aos termos da consulta, já tratados, posteriormente atribui pesos aos termons da consulta relacionando-os com um determinado documento e então os compara tratando os pesos como vetores e aplicando o cosseno do angulo formado pelos dois vetores (o da consulta e o que relaciona os termos da consulta com os documentos da base de dados).

O algoritmo é bastante útil quando se deseja retornar ao usuário uma resposta semelhante ao que foi pesquisado e não necessáriamente a informação inserida tem que estar 100% certa ou parecida com o que contém o documento.

O modelo vetorial foi escolhido por que dentre os outros ele foi o que apresentou as melhores respostas e a melhor satisfação em relação a busca.
Esta aplicação foi apresentada como trabalho da disciplina ORI (Organização e recuperação da informação) do curso de Sistemas de Informação - UFU. A nota atingia foi 100%, porém há pontos que podem ser melhorados e serão com o tempo.
