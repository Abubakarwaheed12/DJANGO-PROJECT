document.getElementById('btn').addEventListener('click' , MakeReq)

// Simple 
// function MakeReq(){
//     fetch('https://jsonplaceholder.typicode.com/posts')
//     .then((res)=>{
//         if(!res.ok){
//             throw Error(res.statusText)
//         }
//         return res.json()
//     })
//     .then((data)=>{
//         // console.log(data)
//         let count=0
//         let output=document.getElementById('divdata')
//         data.forEach(element => {
//          output.innerHTML+=`<div> ${element.userId} </div>
//          <div> ${element.title} </div> 
//          <div> ${element.body} </div>  `
//             count+=1
//          //  console.log(element.userId)
//          // document.getElementById('divdata').innerText+=`<div> ${data[i].userId} '</div>'` 

//         });
//         // Print The Numbers Of Total Data
//         console.log(count)
//     })
//     .catch((error)=>{
//         console.log(error)
//     })
// }


// With Async 
async function MakeReq(){
    await fetch('https://jsonplaceholder.typicode.com/posts')
    .then((res)=>{
        if(!res.ok){
            throw Error(res.statusText)
        }
        return  res.json()
    })
    .then((data)=>{
        // console.log(data)
        
        let count=0
        let output=document.getElementById('divdata')
        data.forEach(element => {
         output.innerHTML+=`<div> ${element.userId} </div>
         <div> ${element.title} </div> 
         <div> ${element.body} </div>  `
            count+=1
         //  console.log(element.userId)
         // document.getElementById('divdata').innerText+=`<div> ${data[i].userId} '</div>'` 

        });
        // Print The Numbers Of Total Data
        console.log(count)
    })
    .catch((error)=>{
        console.log(error)
    })
}
