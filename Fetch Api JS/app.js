console.log('hello world')

const newReq=fetch(url , {
    method:'POST',
    headers:{
        'accept':'application/json',
        'content-type':'application/json',
    },
    body:body,
    cache:'default',
})