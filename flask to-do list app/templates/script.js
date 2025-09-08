const taskinput = document.querySelector('#task');
const btn = document.querySelector('button');
const list = document.querySelector('ul');



btn.addEventListener('click',()=>
{
    if (taskinput.value.trim() === "") return;
    let listitem = document.createElement('li');
    listitem.innerHTML = taskinput.value;
    list.appendChild(listitem);

    taskinput.value = '';
})

// taskinput.addEventListener('keypress', function(e) {
//     if (e.key === 'Enter') addTask();
// });
