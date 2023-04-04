const selectsElement = document.querySelectorAll(".titleDiv__selectElement");
const arraySelectsElement = Array.from(selectsElement);

// DECLARAR ARRAY COM OS IDS PARA OS GRAFICOS DE DETERMINADO SLOT
const arrayIdsRawDatas = [
  "dashboardRawDatas__water",
  "dashboardRawDatas__energy",
];

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
