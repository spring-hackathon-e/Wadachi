// TODO: personalLogに関してはそもそもいる認識かを確認
// 各モーダル定義
const addChannelModal = document.getElementById("add-channel-modal");
const deleteChannelModal = document.getElementById("delete-channel-modal");
const deleteStudyLogModal = document.getElementById("delete-log-modal");
const editGoalModal = document.getElementById("edit-goal-modal");
const withdrawalModal = document.getElementById("withdrawal-modal");
const updateChannelModal = document.getElementById("update-channel-modal");

// モーダルを開くボタン定義
const addChannelBtn = document.getElementById("add-channel-btn");
const deleteChannelBtn = document.getElementsByClassName("delete-channel-btn");
// TODO: 保留：学習記録削除ボタン(index内自分の記録をクリックした時に削除する？　どんな感じで削除??)
const editGoalBtn = document.getElementById("edit-goal-btn");
const updateChannelBtn = document.getElementById("update-channel-btn");
const withdrawalBtn = document.getElementById("withdrawal-btn");

// modalOpenに各モーダルを開くための引数を渡す
// TODO: 保留：学習記録削除
addChannelBtn.addEventListener("click", () => {
  modalOpen("addChannel");
});
deleteChannelBtn.addEventListener("click", () => {
  modalOpen("deleteChannel");
});
editGoalBtn.addEventListener("click", () => {
  modalOpen("editGoal");
});
updateChannelBtn.addEventListener("click", () => {
  modalOpen("updateChannel");
});
withdrawalBtn.addEventListener("click", () => {
  modalOpen("withdrawalConfirm");
});

// modalOpen(引数)でモーダルを開く
// TODO: 保留：学習記録削除
function modalOpen(mode) {
  if (mode === "addChannel") {
    addChannelModal.style.display = "block";
  } else if (mode === "deleteChannel") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "editGoal") {
    editGoalModal.style.display = "block";
  } else if (mode === "updateChannel") {
    updateChannelModal.style.display = "block";
  } else if (mode === "withdrawalConfirm") {
    withdrawalModal.style.display = "block";
  }
}

// モーダル閉じるボタン
// モーダルのsubmitボタン
const addChannelConfirmBtn = document.getElementById(
  "add-channel-confirmation-btn"
);
const deleteChannelConfirmBtn = document.getElementById(
  "delete-channel-confirmation-btn"
);
const deleteStudyLogCompleteBtn = document.getElementById(
  "delete-log-complete-btn"
);
const setGoalCompleteBtn = document.getElementById("set-goal-complete-btn");
const updateChannelCompleteBtn = document.getElementById(
  "update-channel-complete-btn"
);
const quitCompleteBtn = document.getElementById("quit-complete-btn");

// モーダル内のバツ印ボタン定義
// TODO: 保留：学習記録削除関連
const addPageButtonClose = document.getElementById("add-page-close-btn");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");
const editGoalButtonClose = document.getElementById("edit-goal-close-btn");
const updateChannelButtonClose = document.getElementById(
  "update-channel-close-btn"
);
const withdrawalButtonClose = document.getElementById("withdrawal-close-btn");

// modalCloseに各モーダルを閉じる為の引数を渡す
// TODO: 保留 バツ印ボタンはサンプルから取ってきた処理２個以外保留中(HTMLのバツじるし)
(addChannelConfirmBtn || addPageButtonClose).addEventListener("click", () => {
  modalClose("addChannel");
});
(deleteChannelConfirmBtn || deletePageButtonClose).addEventListener(
  "click",
  () => {
    modalClose("deleteChannel");
  }
);
(setGoalCompleteBtn || editGoalButtonClose).addEventListener("click", () => {
  modalClose("editGoal");
});
(updateChannelCompleteBtn || updateChannelButtonClose).addEventListener(
  "click",
  () => {
    modalClose("updateChannel");
  }
);
(quitCompleteBtn || withdrawalButtonClose).addEventListener("click", () => {
  modalClose("withdrawalConfirm");
});

// TODO: 保留：学習記録削除の処理も後でここに追加
// modalCloseでモーダルを閉じる
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
  }
}
