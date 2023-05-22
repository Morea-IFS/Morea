const arraySelectsElement = Array.from(
  document.querySelectorAll(".titleDiv__selectElement")
);

const iframesRaw = Array.from(
  document.querySelectorAll(".graphicDiv_graphicIframeRaw")
);

const iframesM1h1 = Array.from(
  document.querySelectorAll(".graphicDiv_graphicIframeM1h1")
);

const arrayIdsRawDatas = [];
const arrayIds1h1Datas = [];

const addIdIframesInArray = (arrayIframes, arrayId) => {
  arrayIframes.map((iframe) => {
    arrayId.push(iframe.id);
  });
}


addIdIframesInArray(iframesRaw, arrayIdsRawDatas)
addIdIframesInArray(iframesM1h1, arrayIds1h1Datas)


const addOptions = (arrayForMap, elementSelect) => {
  arrayForMap.map((id, index) => {
    const option = document.createElement("option");
    const nameOption = id.split("-");
    option.value = id;
    option.textContent = nameOption[nameOption.length - 1];
    if (index === 0) {
      option.setAttribute("selected", true);
    }
    elementSelect.appendChild(option);
  });
}

addOptions(arrayIds1h1Datas, arraySelectsElement[0])
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
  toggleGraphic(arrayIds1h1Datas, arraySelectsElement[0]);
  toggleGraphic(arrayIdsRawDatas, arraySelectsElement[1]);
});
