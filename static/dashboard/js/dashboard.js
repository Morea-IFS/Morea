const arraySelectsElement = Array.from(
  document.querySelectorAll(".titleDiv__selectElement")
);
const iframes = Array.from(
  document.querySelectorAll(".graphicDiv_graphicIframe")
);

console.log(arraySelectsElement);

const arrayIdsRawDatas = [];
const arrayIds1h1MeanDatas = []


iframes.map((iframe) => {
  arrayIdsRawDatas.push(iframe.id);
});


const addOptions = (arrayForMap, elementSelect) => {
  arrayForMap.map((id, index) => {
    const option = document.createElement("option");
    option.value = id;
    option.textContent = id;
    if (index === 0) {
      option.setAttribute("selected", true);
    }
    elementSelect.appendChild(option);
  });
}

addOptions(arrayIdsRawDatas, arraySelectsElement[1])


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
