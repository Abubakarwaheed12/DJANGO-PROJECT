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
newReq.then((resolve)=>{
console.log(resolve)
return resolve.text()
})
.then((data)=>{
    console.log(data)
})
.catch((error)=>{
    console.log(error);
})
}


// const axios = require('axios');
// 
// axios.get('/user?ID=12345')
//   .then(function (response) {
    // console.log(response);
//   })
//   .catch(function (error) {
    // console.log(error);
//   })
//   .finally(function () {
    // console.log('you finally function is always runable ')
//   });