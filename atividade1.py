largura  =  input ( 'Coloque a largura do seu comodo em metros: ' )

lenth  =  input ( 'Coloque o cumprimento do seu comodo em metros: ' )

tamanho  =  float ( largura ) *  float ( lenth )

totalProduto  =  tamanho  /  2

formatedText  =  'Será necessário '  +  str (totalProduto ) +  ' litros '  +  ' de '  +  ' produto para a realização da limpeza.'

print ( formatedText )