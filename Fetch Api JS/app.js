// console.log('hello world')

// const newReq=fetch(url , {
//     method:'POST',
//     headers:{
//         'accept':'application/json',
//         'content-type':'application/json',
//     },
//     body:body,
//     cache:'default',
// })

document.getElementById('btn').addEventListener('click' , makeRequest)

function makeRequest(){
    console.log('button clicked')
    console.log('hello world')

const newReq=fetch('data.txt')
newReq.then((resolve)=>console.log(resolve))
}