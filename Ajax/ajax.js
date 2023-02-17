$('.submit').click(function(){
    const xhr=new XMLHttpRequest();

    xhr.open('POST', 'https://dummyjson.com/products/add' , true)

    console.log(xhr)

    xhr.onprogres=function(){
        console.log('On progress')
    }

    xhr.onreadystgrchange=function(){
        console.log(this.responseText)
    }
    name1=$('.name').val()
    age=$('.age').val()
    pass1=$('.password').val()
    data={
        'name':name1,
        'age':age,
        'password':pass1
    }
    console.log(data)
    if(this.status==200){
        console.log('your Status is Okay ')
    }
    xhr.send(data)
}) 


fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))
        
      
console.log(response.id)
console.log('helo wprld') 