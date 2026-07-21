// -------------------------------------------
// Student Portal Accessibility Script
// Hands-On 9
// -------------------------------------------

// Search functionality
const searchInput = document.getElementById("search");
const courseCards = document.querySelectorAll(".course");
const resultCount = document.getElementById("results");

// Update search results
function updateSearch() {

    const keyword = searchInput.value.toLowerCase();

    let visible = 0;

    courseCards.forEach((card) => {

        const title = card.querySelector("h3").textContent.toLowerCase();

        if (title.includes(keyword)) {

            card.style.display = "block";
            visible++;

        } else {

            card.style.display = "none";

        }

    });

    resultCount.textContent = `${visible} Courses Found`;

}

// Search event
searchInput.addEventListener("input", updateSearch);

// -------------------------------------------
// Keyboard Accessibility
// -------------------------------------------

courseCards.forEach((card) => {

    card.addEventListener("keydown", (event) => {

        if (event.key === "Enter") {

            card.querySelector("button").click();

        }

    });

});

// -------------------------------------------
// Enroll Button
// -------------------------------------------

const buttons = document.querySelectorAll(".course button");

buttons.forEach((button) => {

    button.addEventListener("click", () => {

        alert("Course Enrolled Successfully!");

    });

});

// -------------------------------------------
// Mobile Menu Example (ARIA Expanded)
// -------------------------------------------

const nav = document.querySelector("nav");

// Create hamburger button
const menuButton = document.createElement("button");

menuButton.textContent = "☰ Menu";

menuButton.setAttribute("aria-expanded", "false");

menuButton.setAttribute("aria-label", "Toggle Navigation Menu");

menuButton.style.marginBottom = "15px";

// Insert before navigation
nav.parentNode.insertBefore(menuButton, nav);

menuButton.addEventListener("click", () => {

    const expanded =
        menuButton.getAttribute("aria-expanded") === "true";

    menuButton.setAttribute(
        "aria-expanded",
        !expanded
    );

    if (expanded) {

        nav.style.display = "none";

    } else {

        nav.style.display = "block";

    }

});

// Hide menu initially on small screens
if (window.innerWidth < 768) {

    nav.style.display = "none";

}

// -------------------------------------------
// Keyboard Tab Order Check
// -------------------------------------------

document.addEventListener("keydown", (event) => {

    if (event.key === "Tab") {

        console.log("Keyboard Navigation Working");

    }

});

// -------------------------------------------
// Browser Feature Detection
// -------------------------------------------

if ("querySelector" in document) {

    console.log("Browser Supports querySelector");

} else {

    alert("Your browser is outdated.");

}