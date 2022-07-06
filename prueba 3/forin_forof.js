let arre =['elemento1', 'elemento2', 'elemento3'];

arre.nuevapropiedad = 'prop';

//clave hace referencia a las claves en el objeto
//for in devuelve los indices de los objetos
console.log('%c for..in en un arreglo ');
for(let clave in arre){
    console.log(clave);
}

console.log('%c for...of en un arreglo ');

//valor hace referencia a los valores en el objeto
//for of dependiendo del metodo iterador 
for(let valor of arre){
    console.log(valor)
}

console.log(arre[Symbol.iterator]);