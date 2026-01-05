const imgpaths = ["f1.jpg", "f2.jpg", "f3.jpg", "f4.jpg"];
let imgindex = 1;

function slide() {
    imgindex = (imgindex + 1) % imgpaths.length
    let bgsliding = document.getElementById("imgbg");
    const current_img_path = imgpaths[imgindex];
    bgsliding.style.backgroundImage = `url('${current_img_path}')`;
}
setInterval(slide, 2000)

const elements = document.querySelectorAll('.slide_in');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show');
    }
  });
});

elements.forEach(el => observer.observe(el));


