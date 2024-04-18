// Работа с кнопкой добавления файлов в попап

function BtnFileName() {
  const popupHistoryFile = document.querySelectorAll(".popup-history__file");

  popupHistoryFile.forEach((element) => {
    let label = element.previousElementSibling;
    let labelValue = label.innerHTML;
    
    element.addEventListener("change", (e) => {
      let fileName = element.files[0].name;
      
      if (fileName.length > 20) {
        fileName = fileName.substr(0, 20);
      }
      
      if (fileName) {
        label.innerHTML = fileName;
      } else {
        label.innerHTML = labelValue;
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", BtnFileName);


function BtnFileCommentName() {
  const popupHistoryFile = document.querySelectorAll(".comment-form__file");

  popupHistoryFile.forEach((element) => {
    let label = element.previousElementSibling;
    let labelValue = label.innerHTML;
    
    element.addEventListener("change", (e) => {
      let fileName = element.files[0].name;
      
      if (fileName.length > 20) {
        fileName = fileName.substr(0, 20);
      }
      
      if (fileName) {
        label.innerHTML = fileName;
      } else {
        label.innerHTML = labelValue;
      }
    });
  });
}

document.addEventListener("DOMContentLoaded", BtnFileCommentName);