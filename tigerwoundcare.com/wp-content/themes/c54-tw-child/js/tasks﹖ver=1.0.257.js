
function reveal() {
  var reveals = document.querySelectorAll('.reveal');

  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveals[i].getBoundingClientRect().top;
    var elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add('active');
    } else {
      reveals[i].classList.remove('active');
    }
  }
}

window.addEventListener('scroll', reveal, { passive: true });


function closeMenu(event) {
  const nav = document.getElementById('main-nav');
  if (nav) {
    nav.classList.remove('hidden');
    nav.classList.remove('responsive');
    nav.classList.add('hidden');
  }
}

function toggleMenu(event) {
  const nav = document.getElementById('main-nav-mobile');
  if (nav) {
    nav.classList.toggle('hidden');
    nav.classList.toggle('responsive');
  }
}

function subMenuListener() {
  const submenus = document.getElementsByClassName('sub-menu');
  for (const submenu of submenus) {
    submenu.parentElement.classList.add('has-sub-menu');
    submenu.parentElement.addEventListener('click', (event) => {
      event.stopPropagation();
      submenu.classList.toggle('active');
    });
  }
}

function selectedListener() {
  const nav = document.getElementById('main-nav-list');
  for (const child of nav.children) {
    for (const subchild of child.children) {
      if (subchild.tagName.toLowerCase() == 'a') {
        if (subchild.href == window.location.href) {
          child.classList.add('active-menu-item');
        }
      } else if (subchild.tagName.toLowerCase() == 'ul') {
        for (const subsubchild of subchild.children) {
          if (subsubchild.tagName.toLowerCase() == 'a') {
            if (subsubchild.href == window.location.href) {
              subchild.classList.add('active-menu-item');
            }
          }
        }
      }
    }
  }
}

function scrollVisibility() {
  const fadeIn = document.querySelectorAll('.fadeInOut');
  const body = document.getElementsByTagName('BODY')[0];
  for (let i = 0; i < fadeIn.length; i++) {
    const windowTop = body.getBoundingClientRect().top;
    const windowBottom = body.getBoundingClientRect().bottom;

    const elementTop = fadeIn[i].getBoundingClientRect().top;
    const elementBottom = fadeIn[i].getBoundingClientRect().bottom;
    const elementHeight = fadeIn[i].getBoundingClientRect().height;
    const elementVisible = 100;
    if (elementTop < windowTop + elementVisible && elementBottom > 80) {
      fadeIn[i].classList.add('active');
    } else if (windowTop - elementHeight < windowTop - elementVisible) {
      fadeIn[i].classList.remove('active');
    } else {
      fadeIn[i].classList.remove('active');
    }
  }
}

function resizeElements() {
  console.log('do Resize');
  closeMenu();
}

const imagetextblocks = [];

const imageblocks = [];

function runAfterLoaded() {
  console.log('run After Loaded');
  resizeElements();
  scrollVisibility();
  subMenuListener();
  selectedListener();

  window.addEventListener('scroll', scrollVisibility, { passive: true });
  /*window.addEventListener('scroll', scrollDividerVisibility, { passive: true });*/
  window.addEventListener('resize', resizeElements);
}

document.addEventListener('DOMContentLoaded', runAfterLoaded);


