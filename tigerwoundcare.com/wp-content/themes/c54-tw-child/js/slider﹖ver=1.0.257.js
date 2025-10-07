sliderCount = 0;

items = [];
count = {
    default: 0,
};
visibleItems = [];
maxVisible = {
    default: 2,
    topics: 2,
    science: 1,
    products: 1,
    facility: 1,
    customer_service: 1,
    healpack: 4,
};
itemList = {
    default: [],
    products: [],
    science: [],
    topics: [],
    facility: [],
    customer_service: [],
    healpack: [],
};
visibleList = {
    default: [],
};
countList = {
    default: 0,
}

prepareSlider = (key = "default") => {
    key = key.trim();
    visibleList[key] = [];
    count[key] = 0;
    console.log('prepare slider', key, maxVisible[key]);
    for (let item of itemList[key]) {
        console.log('item', item);
        if (count[key] >= maxVisible[key]) {
            let el = document.getElementById(item);
            if (el) {
                console.log('el count 1', el)
                el.style.display = 'none';
                el.style.order = count[key];
                let numel = document.getElementById(item + "_num");
                if (numel) {
                    numel.style.display = 'none';
                    numel.style.order = count[key];
                }
            }
        } else {
            let el = document.getElementById(item);
            console.log('check el', el)
            if (el) {
                console.log('check el, el exist')
                el.style.order = count[key];
                visibleList[key].push(count[key]);
            } else {
                console.log('check el, el not exist')
            }
        }
        count[key] += 1;
    }
    if (itemList[key].length > 0) {
        goTo(itemList[key][0], key);
    }
}

goTo = (item, key = "default") => {
    key = key.trim();
    item = item.trim();
    let newVisible = [];
    console.log('goto', key, item);
    try {
        let el = document.getElementById(itemList[key][visibleList[key][0]]);
        if (el) {
            console.log('el found');
            el.style.display = 'none';
            try {
                let linkOld = document.getElementById('link_' + itemList[key][visibleList[key][0]]);
                if (linkOld)
                    console.log('link old found');
                linkOld.classList.remove('active');
            } catch {
            }
            try {
                let numel = document.getElementById(itemList[key][visibleList[key][0]] + "_num");
                if (numel) {
                    numel.style.display = 'none';
                }
            } catch {
            }
            console.log('itemList', key, itemList[key].length, itemList[key]);

            for (let i = 0; i < itemList[key].length; i++) {
                console.log('searching', item, itemList[key][i]);
                if (itemList[key][i] == item) {
                    newVisible.push(i);
                    break;
                }
            }
            console.log('newVisible', newVisible);
            try {
                let el3 = document.getElementById(itemList[key][newVisible[0]]);
                if (el3) {
                    el3.style.order = 0;
                    el3.style.display = 'inline-grid';
                }
            } catch {

            }
            let numel = document.getElementById(itemList[key][newVisible[0]] + "_num");
            if (numel) {
                numel.style.display = 'inline-grid';
            }
            let linkel = document.getElementById('link_' + itemList[key][newVisible[0]]);
            if (linkel) {
                linkel.classList.add('active');
            }
            visibleList[key] = newVisible;

        } else {
        }
    } catch (e) {
    }
}

nextItem = (key = "default") => {
    key = key.trim();
    let newVisible = [];
    //console.log(key, itemList, visibleList);
    let el = document.getElementById(itemList[key][visibleList[key][0]]);
    el.style.display = 'none';

    if (maxVisible[key] > 1) {
        newVisible.push(visibleList[key][1]);
        if (visibleList[key][1] >= itemList[key].length - 1) {
            newVisible.push(0);
        } else {
            newVisible.push(visibleList[key][1] + 1);
        }
        let el3 = document.getElementById(itemList[key][newVisible[0]]);
        el3.style.order = 0;
        let el2 = document.getElementById(itemList[key][newVisible[1]]);
        el2.style.display = 'inline-grid';
        el2.style.order = 1;
    } else {
        if (visibleList[key][0] >= itemList[key].length - 1) {
            newVisible.push(0);
        } else {
            console.log(itemList[key][visibleList[key][0] + 1]);
            newVisible.push(visibleList[key][0] + 1);
            console.log(newVisible);
        }
        let el3 = document.getElementById(itemList[key][newVisible[0]]);
        el3.style.order = 0;
        el3.style.display = 'inline-grid';
    }
    visibleList[key] = newVisible;
}

prevItem = (key = "default") => {
    key = key.trim();
    let newVisible = [];
    let el = document.getElementById(itemList[key][visibleList[key][0]]);
    el.style.display = 'none';
    if (maxVisible[key] > 1) {
        newVisible.push(visibleList[key][1]);
        if (visibleList[key][1] == 0) {
            newVisible.push(itemList[key].length - 1);
        } else {
            newVisible.push(visibleList[key][1] - 1);
        }
        let el3 = document.getElementById(itemList[key][newVisible[0]]);
        el3.style.order = 0;
        let el2 = document.getElementById(itemList[key][newVisible[1]]);
        el2.style.display = 'inline-grid';
        el2.style.order = 1;
    } else {
        if (visibleList[key][0] == 0) {
            newVisible.push(itemList[key].length - 1);
        } else {
            newVisible.push(visibleList[key][0] - 1);
        }
        let el3 = document.getElementById(itemList[key][newVisible[0]]);
        el3.style.order = 0;
        el3.style.display = 'inline-grid';
    }
    visibleList[key] = newVisible;
}


setActive = () => {
    const path = window.location.pathname;
    let el = document.getElementById('main-nav');
    let found = false;
    for (let nav of el.children) {
        for (let child of nav.children) {
            for (let subchild of child.children) {
                if (subchild.tagName == 'A') {
                    if (subchild.pathname == path) {
                        //console.log('equal', path)
                        child.classList.add('active');
                        subchild.classList.add('active');
                        found = true;
                        break;
                    }
                }
                for (let subsubchild of subchild.children) {
                    if (subsubchild.tagName == 'LI') {
                        //console.log('subsubchild', subsubchild);
                        for (let subsubsubchild of subsubchild.children) {
                            if (subsubsubchild.tagName == 'A') {
                                if (subsubsubchild.pathname == path) {
                                    //          console.log('equal', path)
                                    child.classList.add('active');
                                    subsubchild.classList.add('active');
                                    subsubsubchild.classList.add('active');
                                    found = true;
                                    break;
                                }
                            }
                        }
                        if (found == true) {
                            break;
                        }
                    }
                }
                if (found == true) {
                    break;
                }
            }
            if (found == true) {
                break;
            }

        }
        if (found == true) {
            break;
        }
    }

}


class Slider {
    constructor(element, key = "default") {
        console.log('New Slider for', key);
        this.element = element;
        this.slides = element.querySelectorAll('.slide');
        //this.currentIndex = 0;
        this.key = key;
        this.intervalId = null;
        this.isVisible = false;
        this.init();
        this.setupObserver();
        this.setupHover();
    }

    // Initialize slider
    init() {
        //this.showSlide(this.currentIndex);
    }

    // Show specific slide
    showSlide(index) {
        //this.slides.forEach(slide => slide.classList.remove('active'));
        //this.slides[index].classList.add('active');

    }

    // Next slide
    nextSlide() {
        //this.currentIndex = (this.currentIndex + 1) % this.slides.length;
        //this.showSlide(this.currentIndex);
        console.log('nextSlide', this.key);
        nextItem(this.key);
    }

    // Start autoplay
    startAutoplay() {
        if (!this.intervalId) {
            this.intervalId = setInterval(() => this.nextSlide(), 3000); // 3000ms = 3 seconds
        }
    }

    // Stop autoplay
    stopAutoplay() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    // Setup Intersection Observer
    setupObserver() {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach(entry => {
                    this.isVisible = entry.isIntersecting;
                    if (this.isVisible) {
                        this.startAutoplay();
                    } else {
                        this.stopAutoplay();
                    }
                });
            },
            {
                threshold: 0.5 // Trigger when 50% of slider is visible
            }
        );
        observer.observe(this.element);
    }

    // Pause on hover
    setupHover() {
        this.element.addEventListener('mouseenter', () => this.stopAutoplay());
        this.element.addEventListener('mouseleave', () => {
            if (this.isVisible) this.startAutoplay();
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    setActive();
});

document.addEventListener('DOMContentLoaded', () => {
    // Get all sliders on the page
    // Slider functionality class

    // Initialize all sliders
    // sliders.forEach(slider => new Slider(slider));
});


function menuItemSelect(event) {
    event.preventDefault();
    event.stopPropagation();
    console.log(event);
    let opened = document.getElementById('main-nav');
    let childs = opened.querySelectorAll('.open');
    let parent = event.target.parentElement;
    childs.forEach((child) => {
        if (parent.contains(child) || child.contains(parent)) {
        } else {
            child.classList.remove('open');
        }
    });
    event.target.parentElement.classList.toggle('open');

}