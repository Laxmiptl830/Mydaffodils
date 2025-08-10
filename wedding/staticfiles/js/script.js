function toggleNavLinks() {
    const navLinks = document.querySelector(".navlinks");
    const menuBtn = document.querySelector(".menu i");
    const margin =document.querySelector(".logo");

    // Check if navLinks is currently hidden
    const isHidden = navLinks.style.display === "none" || navLinks.style.display === "";

    if (isHidden) {
        // Show nav links
        navLinks.style.display = "block";
        // Change icon to X
        menuBtn.className = "fa-solid fa-xmark";

        margin.style.marginTop="25px";
    } else {
        // Hide nav links
        navLinks.style.display = "none";
        // Change icon to hamburger
        menuBtn.className = "fa-solid fa-bars";
        margin.style.marginTop="0px";
    }

    console.log("toggled");
}
