document.getElementById('btn').addEventListener('click', postReq)

async function postReq(){
   
    const myinits={
    method:'POST',
        headers:{
            'Content-Type':'application/json',
            'Access-Control-Allow-Credentials': 'true'
        },
        body:"{'name':'abu bakar waheed' , 'job':'web dev'}",
        }
    fetch('https://reqres.in/api/users' , myinits)
    .then((response)=>{
        if(!response.ok){
            throw Error(response.statusText) 
        }
        return response.json()
    })
    .then((data)=>{
        console.log(data)
    })
    .catch((error)=>{
        console.log(error)
    })

}