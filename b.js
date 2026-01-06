// показываем alert, чтобы получить взаимодействие
alert("Нажмите ОК, чтобы продолжить!");

// создаем overlay, который блокирует всю вкладку
let overlay = document.createElement('div');
overlay.style.position = "fixed";
overlay.style.top = 0;
overlay.style.left = 0;
overlay.style.width = "100vw";
overlay.style.height = "100vh";
overlay.style.backgroundColor = "black";
overlay.style.zIndex = 9999;

// блокируем мышку и клавиатуру
overlay.addEventListener('click', e => e.stopPropagation());
overlay.addEventListener('mousedown', e => e.stopPropagation());
overlay.addEventListener('mouseup', e => e.stopPropagation());
overlay.addEventListener('mousemove', e => e.stopPropagation());
overlay.addEventListener('keydown', e => e.preventDefault());
overlay.addEventListener('keyup', e => e.preventDefault());
overlay.addEventListener('keypress', e => e.preventDefault());

document.body.appendChild(overlay);

// создаем видео
let video = document.createElement('video');
video.src = "https://cdn.jsdelivr.net/gh/nikita133724/a/main/Nn.mp4"; // замените на свой файл
video.autoplay = true;
video.controls = false; // скрыть элементы управления
video.style.width = "100%";
video.style.height = "100%";
video.style.objectFit = "cover";

overlay.appendChild(video);

// в случае попытки закрыть видео через Esc или клик
video.addEventListener('contextmenu', e => e.preventDefault());