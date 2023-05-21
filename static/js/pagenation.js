const pagination = () => {
  // 初期設定
  let page = 1; // 今何ページ目にいるか
  const STEP = 4; // ステップ数（1ページに表示する項目数）
  // 全ページ数 channelsリストの総数/ステップ数の余りの有無で場合分け
  // 余りがある場合はページを１つ余分に追加する
  const TOTAL =
    channels.length % STEP == 0
      ? channels.length / STEP
      : Math.floor(channels.length / STEP) + 1;

  // <ul class="pagination"></ul> の中身(li)を書き換える
  const paginationUl = document.querySelector(".pagination");
  let pageCount = 0;
  while (pageCount < TOTAL) {
    let li = document.createElement("li");
    li.innerText = pageCount + 1;
    paginationUl.appendChild(li);
    pageCount++;
  }

  // <ul class="channel-box"></ul> の中身(li)を書き換える
  const show = (page, STEP) => {
    const ul = document.querySelector(".channel-box");
    // 一度リストを空にする
    ul.innerHTML = "";

    const first = (page - 1) * STEP + 1;
    const last = page * STEP;
    //console.log(user_id.user_id);
    channels.forEach((item, i) => {
      if (i < first - 1 || i > last - 1) return;
      const a = document.createElement("a");
      const li = document.createElement("li");
      const url = `/detail/${item.ch_id}`;
     //console.log(item.user_id);

      // チャンネル名の表示
      const ttl = document.createElement("h2");
      ttl.innerText = item.ch_name;
      a.prepend(ttl);

      // サマリーの表示
      const summ = document.createElement("p");
      summ.innerText = item.summary;
      a.appendChild(summ);
      //a.insertafter(summ, ttl);

      //カテゴリの表示
      const ctgul = document.createElement("ul");
      const ctg1 = document.createElement("li");
      const ctg2 = document.createElement("li");
      ctg1.innerText = item.main_category;
      ctg2.innerText = item.sub_category;
      ctgul.className = 'categorytag';
      ctgul.appendChild(ctg1);
      ctgul.appendChild(ctg2);
      a.append(ctgul);

      ctgul.className = 'categorytag';
      //a.innerText = item.name;

      const urlforid = `/detail/${item.ch_id}`;
      a.setAttribute("href", urlforid);
      li.appendChild(a);

      //// もしチャンネル作成者user_idとuser_idが同じだったら削除ボタンを追加
      if (user_id.user_id == item.user_id) {
        const deleteButton = document.createElement("button");
        deleteButton.innerHTML = '<span><i class="fa-solid fa-trash-can"></i></span>';
        deleteButton.classList.add("trash");
        deleteButton.classList.add("smaller-btn");
        li.appendChild(deleteButton);
        deleteButton.addEventListener("click", () => {
          modalOpen("deleteChannel");
          const confirmationButtonLink = document.getElementById(
            "delete-confirm-link"
          ); // aタグ
          const url = `/delete/${item.ch_id}`;
          confirmationButtonLink.setAttribute("href", url);
        });
        //close-btnクラスを持つボタンをクリックで消す
        let CloseBtn = document.getElementsByClassName("close-btn");
        let ArrayCloseBtn = Array.from(CloseBtn);
        //console.log(CloseBtn);
        ArrayCloseBtn.forEach(function (target) {
          target.addEventListener("click", () => {
            if (addChannelModal !== null) {
              modalClose("addChannel");
              modalClose("deleteChannel");
            }
          });
        });
        // モーダルコンテンツ以外がクリックされた時もモーダルを閉じる
        addEventListener("click", outsideClose);
        function outsideClose(e) {
          if (e.target == addChannelModal) {
            addChannelModal.style.display = "none";
          } else if (e.target == deleteChannelModal) {
            deleteChannelModal.style.display = "none";
          } 
        }
      }//ユーサーが作成者だったらゴミ箱（記述終了）
      /////
      ul.appendChild(li);
    });
  };
  // pagination内で現在選択されているページの番号に色を付ける
  const colorPaginationNum = () => {
    // <ul class="pagination"></ul>内の<li></li>を全て取得し、配列に入れる
    // ループさせて一度全ての<li></li>から　class="colored"を削除
    const paginationArr = [...document.querySelectorAll(".pagination li")];
    console.log(paginationArr);
    paginationArr.forEach((page) => {
      page.classList.remove("colored");
    });
    // 選択されているページに　class="colored"を追加（背景色が変わる）
    paginationArr[page - 1].classList.add("colored");
  };

  // 最初に1ページ目を表示
  show(page, STEP);

  // 前ページ遷移
  document.getElementById("prev").addEventListener("click", () => {
    if (page <= 1) return;
    page = page - 1;
    show(page, STEP);
    colorPaginationNum();
  });

  // 次ページ遷移
  document.getElementById("next").addEventListener("click", () => {
    if (page >= channels.length / STEP) return;
    page = page + 1;
    show(page, STEP);
    colorPaginationNum();
  });
};

window.onload = () => {
  pagination();
};
