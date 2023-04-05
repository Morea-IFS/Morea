const selectsElement = document.querySelectorAll(".titleDiv__selectElement");
const arraySelectsElement = Array.from(selectsElement);
const iframes = Array.from(
  document.querySelectorAll(".graphicDiv_graphicIframe")
);
const arrayIdsRawDatas = [];

iframes.map((iframe) => {
  arrayIdsRawDatas.push(iframe.id);
});

arrayIdsRawDatas.map((id) => {
  const option = document.createElement("option");
  option.value = id;
  option.textContent = id;
  arraySelectsElement[1].appendChild(option);
});

// DECLARAR ARRAY COM OS IDS PARA OS GRAFICOS DE DETERMINADO SLOT

const toggleGraphic = (classArray, selectElement) => {
  classArray.map((classData) => {
    if (classData === selectElement.value) {
      let enabladeOption = document.querySelector(`#${selectElement.value}`);
      enabladeOption.classList.add("enableGraphic");
    } else {
      let disabledOption = document.querySelector(`#${classData}`);
      disabledOption.classList.remove("enableGraphic");
    }
  });
};

addEventListener("change", () => {
  toggleGraphic(arrayIdsRawDatas, arraySelectsElement[1]);
});
