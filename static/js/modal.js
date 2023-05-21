// 各モーダル定義
const addChannelModal = document.getElementById("add-channel-modal");
const deleteChannelModal = document.getElementById("delete-channel-modal");
const deleteLogModal = document.getElementById("delete-log-modal");
const deleteStudyLogModal = document.getElementById("delete-log-modal");
const editGoalModal = document.getElementById("edit-goal-modal");
const withdrawalModal = document.getElementById("withdrawal-modal");
const updateChannelModal = document.getElementById("update-channel-modal");

// モーダルを開くボタン定義
const addChannelBtn = document.getElementById("add-channel-btn");
const deleteChannelBtn = document.getElementById("delete-channel-btn");
const deleteLogBtn = document.getElementById("delete-studylog-btn");
const editGoalBtn = document.getElementById("edit-goal-btn");
const updateChannelBtn = document.getElementById("channel-update");
const withdrawalBtn = document.getElementById("withdrawal-btn");


// modalOpenに各モーダルを開くための引数を渡す
if (editGoalBtn !== null) {
  editGoalBtn.addEventListener("click", () => {
    modalOpen("editGoalBtn");
  });
  withdrawalBtn.addEventListener("click", () => {
    modalOpen("withdrawalConfirm");
  });
} else if (updateChannelBtn !== null) {
  updateChannelBtn.addEventListener("click", () => {
    modalOpen("updateChannel");
  });
} else if(addChannelBtn !== null){
  addChannelBtn.addEventListener("click", () => {
  modalOpen("addChannel");  
  });
} else if(deleteChannelBtn !== null){
deleteChannelBtn.addEventListener("click", () => {
  modalOpen("deleteChannel");
  });
}else if(deleteLogBtn !== null){
  deleteLogBtn.addEventListener("click", () => {
    modalOpen("deletelog");
  });
}

// modalOpen(引数)でモーダルを開く
function modalOpen(mode) {
//  console.log(mode);
  if (mode === "addChannel" || addChannelModal !== null) {
    if(mode === "addChannel"){
      addChannelModal.style.display = "block";
    }else if(
      mode === "deleteChannel"){
    deleteChannelModal.style.display = "block";
  }
  } else if (mode === "editGoal" || editGoalModal !== null) {
    editGoalModal.style.display = "block";
  } else if (mode === "updateChannel" || updateChannelModal !== null) {
    updateChannelModal.style.display = "block";
  } else if (mode === "withdrawalConfirm" || withdrawalModal !== null) {
    withdrawalModal.style.display = "block";
  } else if (mode === "deletelog" || deleteLogModal !== null) {
    deleteLogModal.style.display = "block";
  }
}

//close-btnクラスを持つボタンをクリックで消す
let CloseBtn = document.getElementsByClassName("close-btn");
//念のためletで
let ArrayCloseBtn = Array.from(CloseBtn);
console.log(CloseBtn);

ArrayCloseBtn.forEach(function (target) {
  target.addEventListener("click", () => {
    if (editGoalModal !== null) {
      modalClose("editGoal");
      modalClose("withdrawalConfirm");
    } else if (addChannelModal !== null) {
      modalClose("addChannel");
      modalClose("deleteChannel");
    } else if (updateChannelModal !== null) {
      modalClose("updateChannel");
    } else if (deleteLogModal !== null) {
      modalClose("deletelog");
    }
  });
});

function modalClose(mode) {
  if (mode === "addChannel") {
    addChannelModal.style.display = "none";
  } else if (mode === "deleteChannel") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "editGoal") {
    editGoalModal.style.display = "none";
  } else if (mode === "updateChannel") {
    updateChannelModal.style.display = "none";
  } else if (mode === "withdrawalConfirm") {
    withdrawalModal.style.display = "none";
  } else if (mode === "deletelog") {
    deleteLogModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時もモーダルを閉じる
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  } else if (e.target == deleteStudyLogModal) {
    deleteStudyLogModal.style.display = "none";
  } else if (e.target == editGoalModal) {
    editGoalModal.style.display = "none";
  } else if (e.target == withdrawalModal) {
    withdrawalModal.style.display = "none";
  } else if (e.target == updateChannelModal) {
    updateChannelModal.style.display = "none";
  }else if (e.target == deleteLogModal) {
    deleteLogModal.style.display = "none";
  }
}
