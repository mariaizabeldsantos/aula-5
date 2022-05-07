totalGrades  = [ input ( 'Coloque a primeira nota do estudante: ' )
, input ( 'Coloque a segunda nota do estudante: ' )
, input ( 'Coloque a terceira nota do estudante: ' )
, input ( 'Coloque a quarta nota do estudante: ' )]

total  =  float ( totalGrades [ 0 ]) +  float ( totalGrades [ 1 ]) +  float ( totalGrades [ 2 ]) +  float ( totalGrades [ 3 ])

notasMedia  =  total  /  4

formatedText  =  'A mídia da nota do aluno é de '  +  str ( notasMedia ) +  '.'

print ( formatedText )