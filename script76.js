console.log("Jai Hind");

let prom1=new Promise((resolve,reject)=>{
    let a=Math.random();
    if(a<0.5){
        reject("no")
    }
    else{
        setTimeout(() => {
            console.log("yes")
            resolve("Adarsh")
        }, 3500);
    }
})
prom1.then((a)=>{   
    console.log(a);
}).catch((err)=>{
    console.log(err)
})




// ########################
 
async function getData(){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            resolve(455)
        }, 3000);
    })
}
async function main(){
console.log("Loading model")
console.log("Loading...")
console.log("Loadinnnnn...")
let data = await getData()
console.log(data)
console.log("Nicely")
}
main()



// ##########################
async function Data() {
    let x= await fetch('https://jsonplaceholder.typicode.com/todos/1')
    let data=await x.json()
    console.log(data)
}
async function set(){
console.log("Loading model")
console.log("Loading...")
console.log("Loadinnnnn...")
let data = await Data()
console.log(data)
console.log("Nicely")
}
set()