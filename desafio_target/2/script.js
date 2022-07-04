var valor = 0;

//recupera o valor do textbox html
function pega_valor(){
    valor = document.getElementById('valor').value
    
    if (valor == ""){
        alert('O campo está em branco digite novamente.')
        exit();
    }
}

/*Fiz a função pensando na posição individual de cada valor
como se fosse um vetor, existem 3 posições de números que importam.

x, y, x+y (novo_val)
0, 1 , 0+1 (novo_val)

Após a soma os valores tem que se mover uma casa para o lado, dessa forma:

X = Y 
Y = Z 

Ao fim dessa operação veremos que o espectro usual para o cálculo se torna
o novo valor + Y, portanto reutilizamos o X que não nos interessa mais 
para guardar o valor de Y e Y o novo valor, dessa forma mantemos uma
variável aberta para receber a soma dos dois (também aproveitando o espaço já alocado).
*/

function test_fibo(){
    var novo_val = 0;
    var  val_y = 1;
    var val_x = 0;

    while (novo_val < valor){
        novo_val = val_x + val_y;
        val_x = val_y;
        val_y = novo_val;
    }
    
    if (novo_val == valor) {
        console.log(novo_val);
        console.log("Pertence a sequência de Fibonacci.");
        alert("Pertence a sequência de Fibonacci");
    }else{
        console.log(novo_val);
        console.log("Não pertence a sequência de Fibonacci.");
        alert("Não pertence a sequência de Fibonacci");
    }
}
