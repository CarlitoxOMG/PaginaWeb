const imagenes = document.querySelectorAll('.img-galeria')
const imagenesLight = document.querySelector('.agregar-imagen')
const contenedorLight = document.querySelector('.imagen-light')
const menu3 = document.querySelector('.menu');

console.log(imagenes)
console.log(imagenesLight)
console.log(contenedorLight)

const imagen1 = [...imagenes].map((imagen) => {
    return imagen.innerHTML;
})

console.log(imagen1)

imagenes.forEach(imagen1 => {
    imagen1.addEventListener('click', ()=>{
        aparecerImagen(imagen1.getAttribute('src'))
    })
})

contenedorLight.addEventListener('click', (e) =>{
    if(e.target !== imagenesLight){
        contenedorLight.classList.toggle('show')
        imagenesLight.classList.toggle('showImage')
        menu3.style.opacity = '1'
    }
})

const aparecerImagen = (imagen1) => {
    imagenesLight.src = imagen1
    contenedorLight.classList.toggle('show')
    imagenesLight.classList.toggle('showImage')
    menu3.style.opacity = '0'


}


// imagenes.forEach(imagen =>{
//     imagen.addEventListener('click', ()=>{
//         alert("auch, me dolio")
//     })
// })