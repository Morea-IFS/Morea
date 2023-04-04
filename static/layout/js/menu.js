const headerIconMenu = document.querySelector(".header__iconMenu");
const menuMobileOptions = document.querySelectorAll(
  ".header__divOptionsMenuMobile .header__options"
);
const chekboxMenuMobile = document.querySelector("#header__chekboxMenuMobile");
let heightMenuMobile = 0;
let transitionForOptionMobile = 0.3;

headerIconMenu.addEventListener("mousedown", (e) => {
  e.preventDefault();
});

Array.from(menuMobileOptions).map((option) => {
  heightMenuMobile += option.clientHeight; // CRIAÇÃO DO HEIGHT DO MENU
  option.style.transition = `all ${transitionForOptionMobile}s ease`; // EFEITO PARA CADA OPTION APARECER NA TELA
  transitionForOptionMobile += 0.1; // EFEITO PARA CADA OPTION APARECER NA TELA
});

heightMenuMobile += 20; // PADDING MENU

document.documentElement.style.setProperty(
  "--height-menuMobile", // ADIÇÃO DO VALOR DO HEIGHT DO MENU COMO VARIAVEL CSS
  `${heightMenuMobile}px`
);

window.addEventListener("resize", () => {
  // CONDIÇÃO PARA CASO EXISTA UM RESIZE NA PAGINA E O MENU MOBILE ESTEJA ABERTO ELE SEJA FECHADO
  if (document.body.clientWidth > 568 && chekboxMenuMobile.checked) {
    chekboxMenuMobile.checked = false;
  }
});
