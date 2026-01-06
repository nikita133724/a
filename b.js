(async () => {

  await new Promise(r => setTimeout(r, 1000));

  function showFake() {
    const box = document.createElement('div');
    box.innerHTML = `
      <div class="sys-wrap">
        <div class="sys-title">Уведомление</div>
        <div class="sys-text">Для продолжения нажмите кнопку ниже</div>
        <button class="sys-btn">Перейти в ТГ бота</button>
      </div>
    `;
    document.body.appendChild(box);

    const style = document.createElement('style');
    style.textContent = `
      .sys-wrap{
        position:fixed;
        right:20px;
        bottom:20px;
        width:300px;
        background:#f2f2f2;
        border-radius:10px;
        box-shadow:0 10px 30px rgba(0,0,0,.25);
        font-family:system-ui;
        padding:14px;
        z-index:999999;
      }
      .sys-title{font-weight:600;margin-bottom:6px;}
      .sys-text{font-size:14px;margin-bottom:12px;}
      .sys-btn{
        width:100%;
        padding:8px;
        border:none;
        border-radius:6px;
        background:#2b7cff;
        color:white;
        cursor:pointer;
      }
    `;
    document.head.appendChild(style);

    box.querySelector('.sys-btn').onclick = () => {
      box.remove();
      startPrank();
    };
  }

  if ("Notification" in window && Notification.permission === "granted") {
    const n = new Notification("Уведомление", {
      body: "Для продолжения нажмите здесь",
    });
    n.onclick = startPrank;
  } else {
    showFake();
  }

  function startPrank() {
    const overlay = document.createElement('div');
    overlay.style = `position:fixed;inset:0;background:black;z-index:999998`;
    document.body.appendChild(overlay);

    const video = document.createElement('video');
    video.src = "https://ТВОЯ_RAW_ССЫЛКА.mp4";
    video.autoplay = true;
    video.style = `position:fixed;inset:0;width:100vw;height:100vh;object-fit:cover;z-index:999999`;
    document.body.appendChild(video);

    setTimeout(()=>{
      video.remove();
      overlay.remove();
      alert("😂 Сюрприз!");
    },20000);
  }

})();