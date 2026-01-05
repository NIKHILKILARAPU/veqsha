// Intersection Observer for animation on scroll into view
const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Get all person cards
const person1 = document.getElementById("person1");
const person2 = document.getElementById("person2");
const person3 = document.getElementById("person3");

// Apply observer to all person cards
[person1, person2, person3].forEach(el => {
    if (el) {
        observer.observe(el);
        el.addEventListener('click', () => {
            console.log(`${el.id} clicked`);
            el.style.cursor = 'pointer';
        });
    }
});