const elementos = document.querySelectorAll('h2'); //seleciona todos os 'h2' da página
const topicos = new Array(); // cria uma Array
elementos.forEach(elemento => { //percorre o conteúdo da variável 'elementos' criando a variável 'elemento'
	topicos.push(elemento.textContent); //preenche a variável 'topicos' com o conteúdo da variável 'elemento'
	const ancora = document.createElement('a'); //cria o elemento 'a' na variável 'ancora'
	ancora.setAttribute('name', elemento.textContent); //atribue a variável a ""tag"" 'name' para se fazer a âncora preenchendo com o ""nome da âncora"" -> 'topo'
	elemento.append(ancora); //adiciona a âncora no final do conteúdo da variável 'elemento'
	const volta = document.createElement('a'); //cria o elemento 'a'
	volta.setAttribute('href','#'); //atribue o 'href' com nome #(utilizado para se voltar ao início da página)
	volta.textContent = '  -  ' + 'Voltar ao topo'; //preenche o conteúdo da variável 'volta' com " - " + "voltar ao topo"
	elemento.append(volta); //adiciona ao fim da variável 'elemento' a variável 'volta'
});
lista = document.querySelector('ol'); //seleciona o elemento 'ol'
topicos.forEach(topico => { //percorre 'tópicos' adicionando 'topico'
	const item = document.createElement('li'); //cria os 'li' inserindo em 'item'
	item.textContent = topico; //adiciona 'topico' no conteúdo de 'item'
	lista.append(item); //'lista' recebe 'item' adionado ao final do conteúdo 
	const lin = document.createElement('a'); //o elemento 'a' é criado no variável 'lin'
	lin.setAttribute('href', `#${topico}`); //o 'href' é atribuído com o name `#${topico}`  
	lin.textContent = ' - ' + topico; //'lin' tem o conteúdo preenchido com ' - ' + 'topico'
	item.append(lin);
});
