// Scroll Up Start
document.addEventListener('DOMContentLoaded', function () {
    const scrollUpButton = document.getElementById('scrollUp');

    const handleScroll = () => {
        const scrollY = window.scrollY;
        const threshold = 100;
        if (scrollY > threshold) {
            scrollUpButton.classList.add('visible');
        } else {
            scrollUpButton.classList.remove('visible');
        }
    };

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth',
        });
    };

    window.addEventListener('scroll', handleScroll);
    scrollUpButton.addEventListener('click', scrollToTop);
});
// Scroll Up end

// Scrolling Row Start
document.addEventListener('DOMContentLoaded', function () {
    var list = document.getElementById('list1');

    list.addEventListener('wheel', function (event) {
        event.preventDefault();
        var delta = event.deltaY || event.detail || event.wheelDelta; // Получаем значение прокрутки
        list.scrollLeft += delta * 0.5;
    });
});
// Scrolling Row End

// nav start
const menu = document.getElementById("menu");
const nav = document.querySelector(".nav__item");
const navLog = document.querySelector(".nav__log");
const opacity = document.querySelector(".opacity");

menu.onclick = () => {
    menu.classList.toggle("openmenu");
    nav.classList.toggle("active_nav");
    navLog.classList.toggle("active_nav");
    opacity.classList.toggle("opacity_act");
    document.body.style.overflow = document.body.style.overflow === 'hidden' ? 'auto' : 'hidden';
};

opacity.onclick = () => {
    menu.classList.remove("openmenu");
    nav.classList.remove("active_nav");
    navLog.classList.remove("active_nav");
    opacity.classList.remove("opacity_act");
    document.body.style.overflow = 'auto';
};
// nav end

// Dropdown Start
document.getElementById("myInput").addEventListener("focus", function () {
    document.getElementById("myDropdown").classList.add("show");
    opacity.classList.add("opacity_act");
    document.body.style.overflow = 'hidden';
});

document.getElementById("myInput").addEventListener("blur", function () {
    document.getElementById("myDropdown").classList.remove("show");
});
// Dropdown End

// 
document.addEventListener("DOMContentLoaded", function () {
    const titleElement = document.getElementById('title');

    const ulElement = document.getElementById('list');
    const chevron = document.querySelector(".fa-chevron-down");

    titleElement.addEventListener('click', function (event) {
        if (ulElement.classList.contains('show')) {
            ulElement.classList.remove('show');
            chevron.classList.remove("rotate");
        } else {
            ulElement.classList.add('show');
            chevron.classList.add("rotate");
        }

        event.stopPropagation();
    });


    ulElement.addEventListener('click', function (event) {
        event.stopPropagation();
    });

    document.addEventListener('click', function () {
        ulElement.classList.remove('show');
        chevron.classList.remove("rotate");
    });
});
// 

//Akkardion Start 
document.addEventListener("DOMContentLoaded", function () {
    const addresses = document.querySelectorAll(".detail__addres");

    addresses.forEach(function (address) {
        const title = address.querySelector(".title");
        const list = address.querySelector(".detail__list");
        const chevron = address.querySelector(".fa-chevron-down");

        title.addEventListener("click", function () {
            addresses.forEach(function (addr) {
                if (addr !== address) {
                    addr.querySelector(".detail__list").classList.remove("address-act");
                    addr.querySelector(".fa-chevron-down").classList.remove("rotate");
                }
            });

            list.classList.toggle("address-act");
            chevron.classList.toggle("rotate");
        });
    });
});

const gallery = document.getElementById("gallery")
const galleryIcon = document.getElementById("gallery-icon")
const galleryList = document.getElementById("gallery-list")

gallery.addEventListener("click", () => {
    galleryIcon.classList.toggle("rotate")
    galleryList.classList.toggle("gallery-act")
})
//Akkardion End 

// Input Pattern Start
function checkUzbekNumber(number) {
    number = number.replace(/\s/g, '');

    if (!number.startsWith("998")) {
        number = "998" + number;
    }

    if (number.length !== 12) {
        return false;
    }

    let formattedNumber = number.slice(0, 3) + " " + number.slice(3, 5) + " " + number.slice(5, 8) + " " + number.slice(8, 10) + " " + number.slice(10);

    return formattedNumber;
}

function formatPhoneNumber() {
    let input = document.getElementById("phoneNumberInput");
    let phoneNumber = input.value;
    let formattedNumber = checkUzbekNumber(phoneNumber);
    if (formattedNumber) {
        input.value = formattedNumber;
    }
}
// 
function checkUzbekNumber1(number) {
    number = number.replace(/\s/g, '');

    if (!number.startsWith("998")) {
        number = "998" + number;
    }

    if (number.length !== 12) {
        return false;
    }

    let formattedNumber = number.slice(0, 3) + " " + number.slice(3, 5) + " " + number.slice(5, 8) + " " + number.slice(8, 10) + " " + number.slice(10);

    return formattedNumber;
}

function formatPhoneNumber1() {
    let input = document.getElementById("phoneInput1");
    let phoneNumber = input.value;
    let formattedNumber = checkUzbekNumber1(phoneNumber);
    if (formattedNumber) {
        input.value = formattedNumber;
    }
}
// 
function checkUzbekNumber2(number) {
    number = number.replace(/\s/g, '');

    if (!number.startsWith("998")) {
        number = "998" + number;
    }

    if (number.length !== 12) {
        return false;
    }

    let formattedNumber = number.slice(0, 3) + " " + number.slice(3, 5) + " " + number.slice(5, 8) + " " + number.slice(8, 10) + " " + number.slice(10);

    return formattedNumber;
}

function formatPhoneNumber2() {
    let input = document.getElementById("phoneInput2");
    let phoneNumber = input.value;
    let formattedNumber = checkUzbekNumber2(phoneNumber);
    if (formattedNumber) {
        input.value = formattedNumber;
    }
}
// Input Pattern End

// Password Start
function checkPasswordMatch() {
    var password1 = document.getElementById("password1").value;
    var password2 = document.getElementById("password2").value;
    var matchMessage = document.getElementById("passwordMatch");

    if (password1 === password2) {
        matchMessage.innerHTML = "";
    } else {
        matchMessage.innerHTML = "Parollar mos kelmadi!";
    }
}
// Password End

// Modal Start
function openModal() {
    document.body.style.overflow = "hidden";
    document.getElementById("modalContent").classList.add("modalActiv");
    document.getElementById("modalOpasitiy").classList.add("modalActiv");
}

function closeModal() {
    document.getElementById("modalContent").classList.remove("modalActiv");
    document.getElementById("modalOpasitiy").classList.remove("modalActiv");
    document.body.style.overflow = "auto";
}

window.onclick = function (event) {
    let modal = document.getElementById("modalContent");
    if (event.target == modal) {
        closeModal();
    }
}
// Modal End

// SubCategory Start
function toggleClass(button) {
    var list1Item = button.closest('.list1__item'); 
    var subCategory = document.querySelector('.subCategory'); 

    var hasClass = list1Item.classList.contains('subCategoryAct');

    var allListItems = document.querySelectorAll('.list1__item');
    allListItems.forEach(function (item) {
        item.classList.remove('subCategoryAct');
    });
    var allSubCategories = document.querySelectorAll('.subCategory');
    allSubCategories.forEach(function (item) {
        item.classList.remove('subCategoryAct');
    });

    if (!hasClass) {
        list1Item.classList.add('subCategoryAct');
        subCategory.classList.add('subCategoryAct');
    }
}
// SubCategory End
